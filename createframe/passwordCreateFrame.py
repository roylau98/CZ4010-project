import tkinter as tk
from util import utilities
from datetime import datetime
from tkinter import messagebox
import uuid

class passwordCreateFrame(tk.Frame):
    def __init__(self, parent, main, database, vaultKey):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(8, weight=1)
        self.columnconfigure(3, weight=1)
        self.main = main
        self.database = database
        self.vaultKey = vaultKey

        self.accountLabelText = tk.StringVar()
        self.accountLabelText.set("Account:")
        self.accountLabel = tk.Label(self, textvariable=self.accountLabelText)
        self.accountEntry = tk.Text(self, width=60, height=1)

        self.usernameLabelText = tk.StringVar()
        self.usernameLabelText.set("Username:")
        self.usernameLabel = tk.Label(self, textvariable=self.usernameLabelText)
        self.usernameEntry = tk.Text(self, width=60, height=1)

        self.passwordLabelText = tk.StringVar()
        self.passwordLabelText.set("Password:")
        self.passwordLabel = tk.Label(self, textvariable=self.passwordLabelText)
        self.passwordEntry = tk.Text(self, width=60, height=1)

        self.saveButton = tk.Button(self, text="Save", command=self.saveLogin)

        self.accountLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.accountEntry.grid(row=1, column=0, sticky='w', padx=10)
        self.usernameLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.usernameEntry.grid(row=3, column=0, sticky='w', padx=10)
        self.passwordLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.passwordEntry.grid(row=5, column=0, sticky='w', padx=10)
        self.saveButton.grid(row=6, column=0, sticky='w', padx=10, pady=5)

    def saveLogin(self):
        account = self.accountEntry.get("1.0", "end-1c")
        username = self.usernameEntry.get("1.0", "end-1c")
        password = self.passwordEntry.get("1.0", "end-1c")

        if (account == "" or username == "" or password == ""):
            messagebox.showwarning(title="Missing information", message="Account/ Username/ Password is missing")
            return

        encrypted, iv = utilities.encrypt(self.vaultKey, bytes(password, "utf-8"))
        json = {'account': account,
                'username': username,
                'password': encrypted.hex(),
                'updated': datetime.now().strftime('%d %b %Y, %I:%M %p'),
                "iv": iv.hex(),
                'key': uuid.uuid4().hex
                }
        # save encrypted password
        self.database.insertRecord("login", json)
        # we still need to display unencrypted password

        json["password"] = password
        self.main.reRenderDetailsFrame(json, "login")
        self.main.changeItemsFrame("login", False)