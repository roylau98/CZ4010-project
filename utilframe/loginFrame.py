import base64
import tkinter as tk
from utilframe.mainApplication import MainApplication
from utilframe.register import registerFrame
from util import utilities
# from util.firebase import Firebase
import configparser
from tkinter import messagebox
import requests
import os

class loginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # self.firebase = Firebase()

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
        if not (os.path.exists(os.path.join(os.getcwd(), f'{username}'))):
            messagebox.showwarning(title="Error", message="No such user on this machine.")
            return
        # try:
        #     # (email | password) as plaintext, (password | username) as salt
        #     decryptionKey = utilities.KDF(email + password, password + username)
        #
        #     config = configparser.ConfigParser()
        #     config.read(f"./{username}/config.ini")
        #     salt = base64.b64decode(config['CONFIGURATION']['salt'])
        #     iv = base64.b64decode(config['CONFIGURATION']['iv'])
        #
        #     # decrypt user uuid
        #     salt = utilities.decrypt(decryptionKey, salt, iv)
        #
        #     # (decryption Key | uuid) as plaintext, (salt | email) as salt
        #     authKey = utilities.KDF(decryptionKey + salt, salt + email.encode())
        #     # auth = self.firebase.authenticate(authKey.hex())
        #     url = "http://localhost:5000/"
        #     response = requests.get(url + authKey.hex())
        #     if response == None:
        #         messagebox.showwarning(title="Error", message="Wrong username/ email/ password!")
        #         self.loginPage()
        #
        #     data = response.json()
        #     with open(f"./{username}/{username}.db", "rb") as f:
        #         binary = f.readlines()
        #         binary = b"".join(binary)
        #
        #     filehash = utilities.hash(binary)
        #     if filehash != data["hash"]:
        #         messagebox.showwarning(title="Error", message="Database possibly tampered.")
        #
        #     vaultKey = utilities.KDF(decryptionKey + password.encode() + salt, authKey + password.encode())
        #     self.destroy()
        #     MainApplication(self.parent, self, data["lastLogin"], vaultKey, username).grid(sticky='nsew')
        #     return username
        # except Exception as e:
        #     messagebox.showwarning(title="Error", message="Wrong username/ email/ password!")
        # (email | password) as plaintext, (password | username) as salt
        decryptionKey = utilities.KDF(email + password, password + username)

        config = configparser.ConfigParser()
        config.read(f"./{username}/config.ini")
        salt = base64.b64decode(config['CONFIGURATION']['salt'])
        iv = base64.b64decode(config['CONFIGURATION']['iv'])

        # decrypt user uuid
        salt = utilities.decrypt(decryptionKey, salt, iv)

        # (decryption Key | uuid) as plaintext, (salt | email) as salt
        authKey = utilities.KDF(decryptionKey + salt, salt + email.encode())

        # auth = self.firebase.authenticate(authKey.hex())
        url = "http://localhost:5000/"
        response = requests.get(url + authKey.hex())
        if response == None:
            messagebox.showwarning(title="Error", message="Wrong username/ email/ password!")
            self.loginPage()

        data = response.json()
        with open(f"./{username}/{username}.db", "rb") as f:
            binary = f.readlines()
            binary = b"".join(binary)

        filehash = utilities.hash(binary)
        if filehash != data["hash"]:
            messagebox.showwarning(title="Error", message="Database possibly tampered.")

        vaultKey = utilities.KDF(decryptionKey + password.encode() + salt, authKey + password.encode())
        # hmac key (authKey | password) plaintext, (UUID | vault key) as salt
        hmacKey = utilities.KDF(authKey + password.encode(), salt + vaultKey)
        self.destroy()
        MainApplication(self.parent, self, data["lastLogin"], vaultKey, username, data["auth"], hmacKey).grid(sticky='nsew')
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