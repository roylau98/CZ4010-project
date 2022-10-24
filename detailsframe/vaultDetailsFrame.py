import tkinter as tk
import utilities


class vaultDetailsFrame(tk.Frame):
    def __init__(self, parent, main, json, itemFrame):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(10, weight=1)
        self.columnconfigure(3, weight=1)
        self.json = json
        self.main = main
        self.itemFrame = itemFrame

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

        self.locationLabelText = tk.StringVar()
        self.locationLabelText.set("Location:")
        self.locationLabel = tk.Label(self, textvariable=self.locationLabelText)
        self.vaultLocation = tk.StringVar()
        self.vaultLocation.set(self.json['path'] + "/" + self.json['filename'])
        self.vaultLocationText = tk.Text(self, width=60, height=1)
        self.vaultLocationText.insert("1.0", self.vaultLocation.get())

        self.decryptButton = tk.Button(self, text="Decrypt", command=self.decryptVault)
        self.editButton = tk.Button(self, text="Edit", command=self.editVault)
        self.deleteButton = tk.Button(self, text="Delete", command=self.deleteVault)

        self.dateUpdatedText = tk.StringVar()
        self.dateUpdatedText.set("Updated: " + self.json['updated'])
        self.dateUpdated = tk.Label(self, textvariable=self.dateUpdatedText)

        self.vaultLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.vaultTitleText.grid(row=1, column=0, sticky='w', padx=10)
        self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.vaultEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        self.locationLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.vaultLocationText.grid(row=5, column=0, sticky='w', padx=10)
        self.decryptButton.grid(row=8, column=0, sticky='w', padx=10, pady=5)
        self.editButton.grid(row=8, column=1, sticky='w', padx=10, pady=5)
        self.deleteButton.grid(row=8, column=2, sticky='e', padx=10, pady=5)
        self.dateUpdated.grid(row=9, column=0, sticky='w', padx=10)
    def decryptVault(self):
        pass
    def editVault(self):
        self.main.renderEditFrame("vault", self.json['key'])

    def deleteVault(self):
        utilities.deleteItem(self.json['path'], self.json['filename'])
        self.main.displayDefaultFrame()
        self.itemFrame.deleteButton(self.json['title'] + '\n' + self.json['path'] + "/" + self.json['filename'])
        utilities.deleteFromJson(self.json['key'], "vault")
        self.main.updateItems(self.json['key'], "vault")