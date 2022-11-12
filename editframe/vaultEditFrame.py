import tkinter as tk
from datetime import datetime

class vaultEditFrame(tk.Frame):
    def __init__(self, parent, main, json, itemFrame, database):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(10, weight=1)
        self.columnconfigure(3, weight=1)
        self.json = json
        self.main = main
        self.itemFrame = itemFrame
        self.database = database
        self.oldKey = self.json['title'] + '\n' + self.json['path'] + "/" + self.json['filename']

        self.vaultLabelText = tk.StringVar()
        self.vaultLabelText.set("Title:")
        self.vaultLabel = tk.Label(self, textvariable=self.vaultLabelText)
        self.vaultTitle = tk.StringVar()
        self.vaultTitle.set(self.json['title'])
        self.vaultTitleText = tk.Text(self, width=60, height=1)
        self.vaultTitleText.insert(tk.END, self.vaultTitle.get())

        self.encryptionLabelText = tk.StringVar()
        self.encryptionLabelText.set("Encryption:")
        self.encryptionLabel = tk.Label(self, textvariable=self.encryptionLabelText)
        self.vaultEncryption = tk.StringVar()
        self.vaultEncryption.set(self.json['encryption'])
        self.vaultEncryptionText = tk.Text(self, width=60, height=1)
        self.vaultEncryptionText.insert("end", self.vaultEncryption.get())

        self.saveButton = tk.Button(self, text="Save", command=self.saveVault)

        self.vaultLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.vaultTitleText.grid(row=1, column=0, sticky='w', padx=10)
        self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.vaultEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        self.saveButton.grid(row=8, column=0, sticky='w', padx=10, pady=5)

    def saveVault(self):
        self.json['title'] = self.vaultTitleText.get("1.0", "end-1c").strip()
        self.json['encryption'] = self.vaultEncryptionText.get("1.0", "end-1c").strip()
        currentDate = datetime.now()
        self.json['updated'] = currentDate.strftime('%d %b %Y, %I:%M %p')
        self.database.updateRecord("vault", self.json)
        # utilities.updateJson(self.json['key'], self.json, "vault")
        self.main.reRenderDetailsFrame(self.json, "vault")
        self.itemFrame.updateItems(self.oldKey,
                                   self.json['title'] + '\n' + self.json['path'] + "/" + self.json['filename'])