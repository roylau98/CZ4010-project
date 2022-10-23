import tkinter as tk
from tkinter import scrolledtext
import utilities

class notesDetailsFrame(tk.Frame):
    def __init__(self, parent, main, json):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(10, weight=1)
        self.columnconfigure(2, weight=1)
        self.json = json
        self.main = main

        self.noteLabelText = tk.StringVar()
        self.noteLabelText.set("Title:")
        self.noteLabel = tk.Label(self, textvariable=self.noteLabelText)
        self.noteTitle = tk.StringVar()
        self.noteTitle.set(self.json['title'])
        self.noteTitleText = tk.Text(self, width=60, height=1)
        self.noteTitleText.insert(tk.END, self.noteTitle.get())

        self.encryptionLabelText = tk.StringVar()
        self.encryptionLabelText.set("Encryption:")
        self.encryptionLabel = tk.Label(self, textvariable=self.encryptionLabelText)
        self.noteEncryption = tk.StringVar()
        self.noteEncryption.set(self.json['encryption'])
        self.noteEncryptionText = tk.Text(self, width=60, height=1)
        self.noteEncryptionText.insert("end", self.noteEncryption.get())

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
        self.decrypted = utilities.decryptNote(self.json['encryption'], self.json['path'], self.json['filename'])
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
        self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.noteEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        self.locationLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.noteLocationText.grid(row=5, column=0, sticky='w', padx=10)
        self.bodyLabel.grid(row=6, column=0, sticky='w', padx=10)
        self.noteBodyText.grid(row=7, column=0, sticky='w', padx=10)
        self.editButton.grid(row=8, column=0, sticky='w', padx=10, pady=5)
        self.deleteButton.grid(row=8, column=1, sticky='e', padx=10, pady=5)
        self.dateUpdated.grid(row=9, column=0, sticky='w', padx=10)

    def editNote(self):
        pass

    def deleteNote(self):
        utilities.deleteItem(self.json['path'], self.json['filename'])
        self.main.displayDefaultFrame()