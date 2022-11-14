import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from util import utilities
import os

class notesDetailsFrame(tk.Frame):
    def __init__(self, parent, main, json, itemFrame, database, vaultKey, hmacKey):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(10, weight=1)
        self.columnconfigure(2, weight=1)
        self.json = json
        self.main = main
        self.itemFrame = itemFrame
        self.database = database
        self.vaultKey = vaultKey
        self.hmacKey = hmacKey

        self.noteLabelText = tk.StringVar()
        self.noteLabelText.set("Title:")
        self.noteLabel = tk.Label(self, textvariable=self.noteLabelText)
        self.noteTitle = tk.StringVar()
        self.noteTitle.set(self.json['title'])
        self.noteTitleText = tk.Text(self, width=60, height=1)
        self.noteTitleText.insert(tk.END, self.noteTitle.get())

        self.hashLabelText = tk.StringVar()
        self.hashLabelText.set("Hash:")
        self.hashLabel = tk.Label(self, textvariable=self.hashLabelText)
        self.noteHash = tk.StringVar()
        self.noteHash.set(self.json['hash'])
        self.noteHashText = tk.Text(self, width=60, height=2)
        self.noteHashText.insert("end", self.noteHash.get())

        self.locationLabelText = tk.StringVar()
        self.locationLabelText.set("Location:")
        self.locationLabel = tk.Label(self, textvariable=self.locationLabelText)
        self.noteLocation = tk.StringVar()
        self.noteLocation.set(self.json['path']+"/"+self.json['filename'])
        self.noteLocationText = tk.Text(self, width=60, height=1)
        self.noteLocationText.insert("1.0", self.noteLocation.get())

        self.bodyLabelText = tk.StringVar()
        self.bodyLabelText.set("Body:")
        self.bodyLabel = tk.Label(self, textvariable=self.bodyLabelText)
        self.noteBody = tk.StringVar()

        if not os.path.isfile(self.json['path']+"/"+self.json['filename']):
            messagebox.showwarning(title="Error", message="File does not exists.")
            self.deleteNote()
            return

        self.decrypted, self.hashed = utilities.decryptNote(self.json['path'], self.json['filename'], self.vaultKey, self.json["iv"], self.hmacKey)

        # if self.hashed != self.json['hash']:
        if not utilities.verifyhashMAC(self.hmacKey, self.decrypted.encode(), self.json["hash"]):
            messagebox.showwarning(title="Warning", message="Hash does not match. Possibly tampered.")

        self.noteBody.set(self.decrypted)
        self.noteBodyText = scrolledtext.ScrolledText(self, width=60, height=18)
        self.noteBodyText.insert("end", self.noteBody.get())

        self.editButton = tk.Button(self, text="Edit", command=self.editNote)
        self.deleteButton = tk.Button(self, text="Delete", command=self.deleteNote)

        self.dateUpdatedText = tk.StringVar()
        self.dateUpdatedText.set("Updated: " + self.json['updated'])
        self.dateUpdated = tk.Label(self, textvariable=self.dateUpdatedText)

        self.noteLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.noteTitleText.grid(row=1, column=0, sticky='w', padx=10)
        self.hashLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.noteHashText.grid(row=3, column=0, sticky='w', padx=10)
        self.locationLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.noteLocationText.grid(row=5, column=0, sticky='w', padx=10)
        self.bodyLabel.grid(row=6, column=0, sticky='w', padx=10)
        self.noteBodyText.grid(row=7, column=0, sticky='w', padx=10)
        self.editButton.grid(row=8, column=0, sticky='w', padx=10, pady=5)
        self.deleteButton.grid(row=8, column=1, sticky='e', padx=10, pady=5)
        self.dateUpdated.grid(row=9, column=0, sticky='w', padx=10)

    def editNote(self):
        self.main.renderEditFrame("notes", self.json['key'])

    def deleteNote(self):
        self.database.deleteRecord("notes", self.json["key"])
        self.main.displayDefaultFrame()
        self.itemFrame.deleteButton(self.json['title'] + '\n' + self.json['path'] + "/" + self.json['filename'])
        self.main.updateItems(self.json['key'], "notes")