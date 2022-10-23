import threading
import tkinter as tk
import string
import time
import utilities
from datetime import datetime

class passwordDetailsFrame(tk.Frame):
    def __init__(self, parent, main, json):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.json = json
        self.parent = parent
        self.rowconfigure(7, weight=1)
        self.columnconfigure(3, weight=1)
        self.main = main

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
        self.usernameCopyButton = tk.Button(self, text="Copy")

        self.passwordLabelText = tk.StringVar()
        self.passwordLabelText.set("Password:")
        self.passwordLabel = tk.Label(self, textvariable=self.passwordLabelText)
        self.passwordEntryText = tk.StringVar()
        self.passwordEntryText.set(self.json['password'])
        self.passwordEntry = tk.Entry(self, text=self.passwordEntryText, width=60, show="*")
        self.passwordCopyButton = tk.Button(self, text="Copy", command=self.copyToClipboard)
        self.passwordViewButton = tk.Button(self, text="View", command=self.unhidePassword)

        self.dateUpdatedText = tk.StringVar()
        self.now = datetime.now()
        self.dateUpdatedText.set("Updated: " + self.now.strftime('%d %b %Y, %I:%M %p'))
        self.dateUpdated = tk.Label(self, textvariable=self.dateUpdatedText)

        self.accountLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.accountEntry.grid(row=1, column=0, sticky='w', padx=10)
        self.usernameLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.usernameEntry.grid(row=3, column=0, sticky='w', padx=10)
        self.usernameCopyButton.grid(row=3, column=1, sticky='e', padx=5)
        self.passwordLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.passwordEntry.grid(row=5, column=0, sticky='w', padx=10)
        self.passwordCopyButton.grid(row=5, column=1, sticky='e', padx=5)
        self.passwordViewButton.grid(row=5, column=2, sticky='e', padx=5)
        self.dateUpdated.grid(row=6, column=0, sticky='w', pady=10, padx=10)

    def copyToClipboard(self):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(self.passwordEntryText.get())
        background = threading.Thread(target=self.clearClipboard, daemon=True)
        background.start()

    def clearClipboard(self):
        time.sleep(10)
        print("Cleared clipboard")
        self.parent.clipboard_clear()
        self.parent.clipboard_append('')

    def unhidePassword(self):
        self.passwordEntry.config(show="")
        background = threading.Thread(target=self.hidePassword, daemon=True)
        background.start()

    def hidePassword(self):
        time.sleep(10)
        print("Hidden password")
        self.passwordEntry.config(show="*")