import base64
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from util import utilities
from datetime import datetime
import uuid

class notesCreateFrame(tk.Frame):
    def __init__(self, parent, main, database, vaultKey, username, hmacKey):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(11, weight=1)
        self.columnconfigure(2, weight=1)
        self.main = main
        self.database = database
        self.vaultKey = vaultKey
        self.username = username
        self.hmacKey = hmacKey

        self.noteLabelText = tk.StringVar()
        self.noteLabelText.set("Title:")
        self.noteLabel = tk.Label(self, textvariable=self.noteLabelText)
        self.noteTitleText = tk.Text(self, width=60, height=1)

        # self.encryptionLabelText = tk.StringVar()
        # self.encryptionLabelText.set("Encryption:")
        # self.encryptionLabel = tk.Label(self, textvariable=self.encryptionLabelText)
        # self.noteEncryptionText = tk.Text(self, width=60, height=1)
        # self.noteEncryptionText.insert("end", "AES-256-CBC")

        # self.locationLabelText = tk.StringVar()
        # self.locationLabelText.set("Location:")
        # self.locationLabel = tk.Label(self, textvariable=self.locationLabelText)
        # self.noteLocation = tk.StringVar()
        # self.noteLocation.set("./notes")
        # self.noteLocationText = tk.Text(self, width=60, height=1)
        # self.noteLocationText.insert("1.0", self.noteLocation.get())

        self.filenameLabelText = tk.StringVar()
        self.filenameLabelText.set("Filename:")
        self.filenameLabel = tk.Label(self, textvariable=self.filenameLabelText)
        self.noteFilenameText = tk.Text(self, width=60, height=1)

        self.bodyLabelText = tk.StringVar()
        self.bodyLabelText.set("Body:")
        self.bodyLabel = tk.Label(self, textvariable=self.bodyLabelText)
        self.noteBodyText = scrolledtext.ScrolledText(self, width=60, height=18)

        self.saveButton = tk.Button(self, text="Save", command=self.saveNote)

        self.noteLabel.grid(row=0, column=0, sticky='w', padx=10)
        self.noteTitleText.grid(row=1, column=0, sticky='w', padx=10)
        #self.encryptionLabel.grid(row=2, column=0, sticky='w', padx=10)
        #self.noteEncryptionText.grid(row=3, column=0, sticky='w', padx=10)
        #self.locationLabel.grid(row=4, column=0, sticky='w', padx=10)
        #self.noteLocationText.grid(row=5, column=0, sticky='w', padx=10)
        self.filenameLabel.grid(row=6, column=0, sticky='w', padx=10)
        self.noteFilenameText.grid(row=7, column=0, sticky='w', padx=10)
        self.bodyLabel.grid(row=8, column=0, sticky='w', padx=10)
        self.noteBodyText.grid(row=9, column=0, sticky='w', padx=10)
        self.saveButton.grid(row=10, column=0, sticky='w', padx=10, pady=5)

    def saveNote(self):
        noteTitle = self.noteTitleText.get("1.0", "end-1c")
        fileName = self.noteFilenameText.get("1.0", "end-1c")
        notebody = self.noteBodyText.get("1.0", "end-1c")

        if (noteTitle == "" or fileName == "" or notebody == ""):
            messagebox.showwarning(title="Missing information", message="Filename/ Title/ Note is missing")
            return

        encryptedNote, iv = utilities.encrypt(self.vaultKey, bytes(notebody, "utf-8"))
        # hashed = utilities.hash(bytes(notebody, "utf-8"))
        hashed = utilities.hashMAC(self.hmacKey, bytes(notebody, "utf-8"))
        json = {'title': noteTitle,
                'filename': fileName,
                'hash': hashed,
                'path': f"./{self.username}/notes",
                'updated': datetime.now().strftime('%d %b %Y, %I:%M %p'),
                # 'iv': iv.hex(),
                "iv": base64.encodebytes(iv),
                'key': uuid.uuid4().hex
                }
        utilities.saveNote(encryptedNote, json['path'], json['filename'])
        self.database.insertRecord("notes", json)
        # json["iv"] = bytes.fromhex(json["iv"])
        json["iv"] = base64.b64decode(json["iv"])
        self.main.reRenderDetailsFrame(json, "notes")
        self.main.changeItemsFrame("notes", False)
