import base64
import tkinter as tk
import configparser
from tkinter import messagebox
#from util.firebase import Firebase
from util import utilities
import uuid
from util.database import DataBase
import os
import requests
from datetime import datetime

class registerFrame(tk.Frame):
    def __init__(self, parent, login):
        super().__init__()
        self.parent = parent
        self.rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.font = ('Times', 14)
        self.login = login

        self.variable = tk.StringVar()
        self.right_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)
        self.usernameLabel = tk.Label(self, text="Enter Username", bg='#CCCCCC', font=self.font)
        self.emailLabel = tk.Label(self, text="Enter Email", bg='#CCCCCC', font=self.font)
        self.passwordLabel = tk.Label(self,text="Enter Password", bg='#CCCCCC', font=self.font)
        self.rePasswordLabel = tk.Label(self,text="Re-Enter Password", bg='#CCCCCC', font=self.font)

        self.register_username = tk.Entry(self, font=self.font)
        self.register_email = tk.Entry(self, font=self.font)
        self.register_pwd = tk.Entry(self, font=self.font, show='*')
        self.pwd_again = tk.Entry(self, font=self.font, show='*')
        self.register_btn = tk.Button(self, width=15, text='Register', font=self.font, relief=tk.SOLID, cursor='hand2', command=self.registerUser)
        self.return_btn = tk.Button(self, width=15, text='Return', font=self.font, relief=tk.SOLID, cursor='hand2',
                                      command=self.returnLogin)

        self.usernameLabel.grid(row=0, column=0, pady=10, padx=20)
        self.emailLabel.grid(row=1, column=0, pady=10, padx=20)
        self.passwordLabel.grid(row=5, column=0, pady=10, padx=20)
        self.rePasswordLabel.grid(row=6, column=0, pady=10, padx=20)
        self.register_username.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=6, column=1, pady=10, padx=20)
        self.register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.return_btn.grid(row=7, column=0, pady=10, padx=20)

    def registerUser(self):
        if (self.register_email.get() == "" or self.register_username.get() == "" or self.register_pwd.get() == ""
                or self.pwd_again.get() == ""):
            messagebox.showwarning("Error", message="Missing fields!")
            return

        if (self.register_pwd.get() != self.pwd_again.get()):
            messagebox.showwarning("Error", message="Entered password does not match!")
            return

        email = self.register_email.get()
        password = self.register_pwd.get()
        username = self.register_username.get()
        #creating folders
        try:
            os.mkdir(f"./{username}")
            os.mkdir(f"./{username}/notes")
            os.mkdir(f"./{username}/vault")
        except Exception as e:
            messagebox.showwarning(title="Error", message="Username taken, please choose another one.")
            return

        salt = bytes(str(uuid.uuid4()), "utf-8")

        # (email | password) as plaintext, (password | username) as salt
        encryptionKey = utilities.KDF(email + password, password + username)
        authKey = utilities.KDF(encryptionKey + salt, salt + email.encode())

        # save encrypted "salt"
        encryptedSalt, iv = utilities.encrypt(encryptionKey, salt)
        config = configparser.ConfigParser()

        config['CONFIGURATION'] = {'salt': base64.encodebytes(encryptedSalt).decode("utf-8"),
                                   'iv': base64.encodebytes(iv).decode("utf-8")}

        with open(f"./{username}/config.ini", 'w') as f:
            config.write(f)

        # creates the database
        database = DataBase(f"./{username}/{username}.db")
        database.setup()
        database.closeConnection()

        with open(f"./{username}/{username}.db", "rb") as f:
            binary = f.readlines()
            binary = b"".join(binary)

        url = "http://localhost:5000/register"
        params = {
            "auth": authKey.hex(),
            "lastLogin": datetime.now().strftime('%d %b %Y, %I:%M %p'),
            "filehash": utilities.hash(binary)
        }
        response = requests.post(url, json=params, headers={'content-type': 'application/json'})
        #firebaseDB = Firebase()
        #firebaseDB.registerUser(authKey.hex())
        if response.status_code == 200:
            messagebox.showinfo(title="Success", message="Successfully registered user!")
        else:
            messagebox.showwarning(title="Error", message="Unable to register user!")
        self.destroy()
        self.login.loginPage()
        # firebaseDB.getLoginDetails(salt.hex())

    def returnLogin(self):
        self.destroy()
        self.login.loginPage()