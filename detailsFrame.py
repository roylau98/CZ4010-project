import threading
import tkinter as tk
import string
import time
import utilities

class detailsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(6, weight=1)
        self.columnconfigure(3, weight=1)

        self.accountLabelText = tk.StringVar()
        self.accountLabelText.set("Account:")
        self.accountLabel = tk.Label(self, textvariable=self.accountLabelText)
        self.accountEntryText = tk.StringVar()
        self.accountEntryText.set("Reddit")
        self.accountEntry = tk.Entry(self, text=self.accountEntryText, width=60)

        self.usernameLabelText = tk.StringVar()
        self.usernameLabelText.set("Username:")
        self.usernameLabel = tk.Label(self, textvariable=self.usernameLabelText)
        self.usernameEntryText = tk.StringVar()
        self.usernameEntryText.set("ABCD")
        self.usernameEntry = tk.Entry(self, text=self.usernameEntryText, width=60)
        self.usernameCopyButton = tk.Button(self, text="Copy")

        self.passwordLabelText = tk.StringVar()
        self.passwordLabelText.set("Password:")
        self.passwordLabel = tk.Label(self, textvariable=self.passwordLabelText)
        self.passwordEntryText = tk.StringVar()
        self.passwordEntryText.set("ABCD")
        self.passwordEntry = tk.Entry(self, text=self.passwordEntryText, width=60, show="*")
        self.passwordCopyButton = tk.Button(self, text="Copy", command=self.copyToClipboard)
        self.passwordViewButton = tk.Button(self, text="View", command=self.unhidePassword)

        self.accountLabel.grid(row=0, column=0, sticky='w')
        self.accountEntry.grid(row=1, column=0, sticky='w')
        self.usernameLabel.grid(row=2, column=0, sticky='w')
        self.usernameEntry.grid(row=3, column=0, sticky='w')
        self.usernameCopyButton.grid(row=3, column=1, sticky='w')
        self.passwordLabel.grid(row=4, column=0, sticky='w')
        self.passwordEntry.grid(row=5, column=0, sticky='w')
        self.passwordCopyButton.grid(row=5, column=1, sticky='w')
        self.passwordViewButton.grid(row=5, column=2, sticky='w')

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