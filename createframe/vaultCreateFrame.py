import base64
import tkinter as tk
from util import utilities
import os
import uuid
from tkinter import messagebox
from datetime import datetime
class vaultCreateFrame(tk.Frame):
    def __init__(self, parent, main, database, vaultKey, username):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(10, weight=1)
        self.columnconfigure(3, weight=1)
        self.main = main
        self.database = database
        self.vaultKey = vaultKey
        self.username = username

        self.vaultLabelText = tk.StringVar()
        self.vaultLabelText.set("Title:")
        self.vaultLabel = tk.Label(self, textvariable=self.vaultLabelText)
        self.vaultTitleText = tk.Text(self, width=60, height=1)

        # self.encryptionLabelText = tk.StringVar()
        # self.encryptionLabelText.set("Hash:")
        # self.encryptionLabel = tk.Label(self, textvariable=self.encryptionLabelText)
        # self.vaultEncryptionText = tk.Text(self, width=60, height=1)
        # self.vaultEncryptionText.insert("end", "AES-256-CBC")

        self.filepathLabelText = tk.StringVar()
        self.filepathLabelText.set("File path:")
        self.filepathLabel = tk.Label(self, textvariable=self.filepathLabelText)
        self.vaultFilepathText = tk.Text(self, width=60, height=2)

        # self.filenameLabelText = tk.StringVar()
        # self.filenameLabelText.set("Filename:")
        # self.filenameLabel = tk.Label(self, textvariable=self.filenameLabelText)
        # self.vaultFilenameText = tk.Text(self, width=60, height=1)

        self.encryptButton = tk.Button(self, text="Encrypt", command=self.encryptVault)

        self.vaultLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.vaultTitleText.grid(row=1, column=0, sticky='w', padx=10)
        #self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        #self.vaultEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        self.filepathLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.vaultFilepathText.grid(row=5, column=0, sticky='w', padx=10)
        #self.filenameLabel.grid(row=6, column=0, sticky='w', padx=10)
        #self.vaultFilenameText.grid(row=7, column=0, sticky='w', padx=10)
        self.encryptButton.grid(row=8, column=0, sticky='w', padx=10, pady=5)

    def encryptVault(self):
        path = self.vaultFilepathText.get("1.0", "end-1c")
        if not os.path.isfile(path):
            messagebox.showwarning(title="Error", message="File does not exists.")
            return

        if "\\" in path:
            path = path.replace("\\", "/")
        path = path.rsplit("/", 1)

        vaultTitle = self.vaultTitleText.get("1.0", "end-1c")
        if (vaultTitle == "" or path[1] == ""):
            messagebox.showwarning(title="Missing information", message="Title/ Filename is missing")
            return

        iv, hash = utilities.encryptFile(self.vaultKey, "/".join(path), f"./{self.username}/vault/" + path[1])
        print(iv)
        json = {
            "title": vaultTitle,
            "filename": path[1],
            "hash": hash,
            "path": f"./{self.username}/vault",
            "updated": datetime.now().strftime('%d %b %Y, %I:%M %p'),
            # "iv": iv.hex(),
            "iv": base64.encodebytes(iv),
            "key": uuid.uuid4().hex
        }

        self.database.insertRecord("vault", json)
        # store iv as bytes
        json["iv"] = base64.b64decode(json["iv"])
        self.main.reRenderDetailsFrame(json, "vault")
        self.main.changeItemsFrame("vault", False)