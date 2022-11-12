import tkinter as tk
from utilframe.mainApplication import MainApplication
from utilframe.register import registerFrame
from util import utilities
from util.firebase import Firebase
import configparser
from tkinter import messagebox

class loginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.firebase = Firebase()

        # username label and text entry box
        self.usernameLabel = tk.Label(self, text="Username: ")
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        # email label and text entry box
        self.emailLabel = tk.Label(self, text="Email: ")
        self.email = tk.StringVar()
        self.emailEntry = tk.Entry(self, textvariable=self.email)

        # password label and password entry box
        self.passwordLabel = tk.Label(self, text="Password: ")
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(self, textvariable=self.password, show='*')

        # login button
        self.loginButton = tk.Button(self, text="Login", command=self.validateLogin)
        self.registerButton = tk.Button(self, text="Register", command=self.registerUser)

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.emailLabel.grid(row=1, column=0)
        self.emailEntry.grid(row=1, column=1)
        self.passwordLabel.grid(row=2, column=0)
        self.passwordEntry.grid(row=2, column=1)
        self.loginButton.grid(row=3, column=0)
        self.registerButton.grid(row=3, column=1)

    def validateLogin(self):
        username = self.usernameEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()

        if (username == "" or email == "" or password == ""):
            messagebox.showwarning(title="Error", message="Missing fields!")
            return

        # (email | password) as plaintext, (password | username) as salt
        decryptionKey = utilities.KDF(email + password, password + username)

        config = configparser.ConfigParser()
        config.read(f"./{username}/config.ini")
        salt = bytes.fromhex(config['CONFIGURATION']['salt'])
        iv = bytes.fromhex(config['CONFIGURATION']['iv'])

        # decrypt user uuid
        salt = utilities.decrypt(decryptionKey, salt, iv)

        # (decryption Key | uuid) as plaintext, (salt | email) as salt
        authKey = utilities.KDF(decryptionKey + salt, salt + email.encode())
        auth = self.firebase.authenticate(authKey.hex())
        if auth == None:
            messagebox.showwarning(title="Error", message="Wrong email/password!")
            return

        vaultKey = utilities.KDF(decryptionKey + password.encode() + salt, authKey + password.encode())
        self.destroy()
        MainApplication(self.parent, self, auth, self.firebase, vaultKey, username).grid(sticky='nsew')
        return username

    def registerUser(self):
        registerFrame(self.parent, self).grid(row=1, column=1)

    def loginPage(self):
        loginFrame(self.parent).grid(row=1, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    loginFrame(root).grid(row=1, column=1)#side="top", fill="both", expand=True)
    root.mainloop()