import tkinter as tk
import json
from functools import partial
from mainApplication import MainApplication
from register import registerFrame

class loginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # username label and text entry box
        self.usernameLabel = tk.Label(self, text="Username: ")
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        # password label and password entry box
        self.passwordLabel = tk.Label(self, text="Password: ")
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(self, textvariable=self.password, show='*')

        # login button
        self.loginButton = tk.Button(self, text="Login", command=self.validateLogin)
        self.registerButton = tk.Button(self, text="Register", command=self.registerUser)

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.loginButton.grid(row=2, column=0)
        self.registerButton.grid(row=2, column=1)

    def validateLogin(self):
        print("username entered :", self.usernameEntry.get())
        print("password entered :", self.passwordEntry.get())
        MainApplication(self.parent).grid(sticky='nsew')
        return

    def registerUser(self):
        self.grid_forget()
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