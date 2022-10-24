import tkinter as tk
from tkinter import scrolledtext
import utilities
from datetime import datetime

class notesEditCreateFrame(tk.Frame):
    def __init__(self, parent, main, json, itemFrame):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(11, weight=1)
        self.columnconfigure(2, weight=1)
        self.json = json
        self.main = main
        self.itemFrame = itemFrame
        self.oldKey = self.json['title'] + '\n' + self.json['path'] + "/" + self.json['filename']

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
        self.noteLocation.set(self.json['path'])
        self.noteLocationText = tk.Text(self, width=60, height=1)
        self.noteLocationText.insert("1.0", self.noteLocation.get())

        self.filenameLabelText = tk.StringVar()
        self.filenameLabelText.set("Filename:")
        self.filenameLabel = tk.Label(self, textvariable=self.filenameLabelText)
        self.noteFilename = tk.StringVar()
        self.noteFilename.set(self.json['filename'])
        self.noteFilenameText = tk.Text(self, width=60, height=1)
        self.noteFilenameText.insert("1.0", self.noteFilename.get())

        self.bodyLabelText = tk.StringVar()
        self.bodyLabelText.set("Body:")
        self.bodyLabel = tk.Label(self, textvariable=self.bodyLabelText)
        self.noteBody = tk.StringVar()
        self.decrypted = utilities.decryptNote(self.json['encryption'], self.json['path'], self.json['filename'])
        self.noteBody.set(self.decrypted)
        self.noteBodyText = scrolledtext.ScrolledText(self, width=60, height=18)
        self.noteBodyText.insert("end", self.noteBody.get())

        self.saveButton = tk.Button(self, text="Save", command=self.saveNote)

        self.noteLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.noteTitleText.grid(row=1, column=0, sticky='w', padx=10)
        self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        self.noteEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        self.locationLabel.grid(row=4, column=0, sticky='w', padx=10)
        self.noteLocationText.grid(row=5, column=0, sticky='w', padx=10)
        self.filenameLabel.grid(row=6, column=0, sticky='w', padx=10)
        self.noteFilenameText.grid(row=7, column=0, sticky='w', padx=10)
        self.bodyLabel.grid(row=8, column=0, sticky='w', padx=10)
        self.noteBodyText.grid(row=9, column=0, sticky='w', padx=10)
        self.saveButton.grid(row=10, column=0, sticky='w', padx=10, pady=5)

    def saveNote(self):
        self.json['title'] = self.noteTitleText.get("1.0", "end-1c").strip()
        self.json['filename'] = self.noteFilenameText.get("1.0", "end-1c").strip()
        self.json['path'] = self.noteLocationText.get("1.0", "end-1c").strip()
        currentDate = datetime.now()
        self.json['updated'] = currentDate.strftime('%d %b %Y, %I:%M %p')
        print(self.json)
        # utilities.updateJson(self.json['key'], self.json, "notes")
        # self.main.reRenderDetailsFrame(self.json, "login")
        # self.itemFrame.updateItems(self.oldKey, self.json['account'] + "\n" + self.json['username'])