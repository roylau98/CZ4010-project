import threading
import tkinter as tk
import time
import utilities
from datetime import datetime

class passwordEditFrame(tk.Frame):
    def __init__(self, parent, main, json, itemFrame, database):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.json = json
        self.parent = parent
        self.rowconfigure(8, weight=1)
        self.columnconfigure(3, weight=1)
        self.main = main
        self.itemFrame = itemFrame
        self.database = database
        self.oldKey = self.json['account'] + "\n" + self.json['username']

        self.accountLabelText = tk.StringVar()
        self.accountLabelText.set("Account:")
        self.accountLabel = tk.Label(self, textvariable=self.accountLabelText)
        self.accountEntryText = tk.StringVar()
        self.accountEntryText.set(self.json['account'])
        self.accountEntry = tk.Entry(self, text=self.accountEntryText, width=60)

        self.usernameLabelText = tk.StringVar()
        self.usernameLabelText.set("Username:")
        self.usernameLabel = tk.Label(self, textvariable=self.usernameLabelText)
        self.usernameEntryText = tk.StringVar()
        self.usernameEntryText.set(self.json['username'])
        self.usernameEntry = tk.Entry(self, text=self.usernameEntryText, width=60)

        self.passwordLabelText = tk.StringVar()
        self.passwordLabelText.set("Password:")
        self.passwordLabel = tk.Label(self, textvariable=self.passwordLabelText)
        self.passwordEntryText = tk.StringVar()
        self.passwordEntryText.set(self.json['password'])
        self.passwordEntry = tk.Entry(self, text=self.passwordEntryText, width=60, show="*")
        self.passwordViewButton = tk.Button(self, text="View", command=self.unhidePassword)

        self.saveButton = tk.Button(self, text="Save", command=self.saveLogin)

        self.accountLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.accountEntry.grid(row=1, column=0, sticky='w', padx=10)
        self.usernameLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.usernameEntry.grid(row=3, column=0, sticky='w', padx=10)
        self.passwordLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.passwordEntry.grid(row=5, column=0, sticky='w', padx=10)
        self.passwordViewButton.grid(row=5, column=1, sticky='e', padx=5)
        self.saveButton.grid(row=6, column=0, sticky='w', padx=10, pady=5)

    def saveLogin(self):
        self.json['account'] = self.accountEntry.get().strip()
        self.json['username'] = self.usernameEntry.get().strip()

        # if password changed, re-encrypt password
        if self.json["password"] != self.passwordEntry.get().strip():
            self.json["iv"] = "abc"
            self.json['password'] = self.passwordEntry.get().strip()

        currentDate = datetime.now()
        self.json['updated'] = currentDate.strftime('%d %b %Y, %I:%M %p')
        self.database.updateRecord("login", self.json)
        # utilities.updateJson(self.json['key'], self.json, "login")
        self.main.reRenderDetailsFrame(self.json, "login")
        self.itemFrame.updateItems(self.oldKey, self.json['account'] + "\n" + self.json['username'])

    def unhidePassword(self):
        self.passwordEntry.config(show="")
        background = threading.Thread(target=self.hidePassword, daemon=True)
        background.start()

    def hidePassword(self):
        time.sleep(10)
        self.passwordEntry.config(show="*")