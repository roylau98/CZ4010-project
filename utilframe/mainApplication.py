from utilframe.passwordGeneratorFrame import passwordGeneratorFrame
from detailsframe.passwordDetailsFrame import passwordDetailsFrame
from detailsframe.notesDetailsFrame import notesDetailsFrame
from detailsframe.defaultDetailsFrame import defaultDetailsFrame
from detailsframe.vaultDetailsFrame import vaultDetailsFrame
from editframe.passwordEditFrame import passwordEditFrame
from editframe.vaultEditFrame import vaultEditFrame
from editframe.notesEditFrame import notesEditFrame
from utilframe.servicesFrame import servicesFrame
from utilframe.itemsFrame import itemsFrame
from createframe.notesCreateFrame import notesCreateFrame
from createframe.passwordCreateFrame import passwordCreateFrame
from createframe.vaultCreateFrame import vaultCreateFrame
from util.database import DataBase
import tkinter as tk
from util import utilities
from datetime import datetime
import requests
import json as js

global user
global authKey
global hKey
global root
def onClose():
    url = "http://localhost:5000/update"
    with open(f"./{user}/{user}.db", "rb") as f:
        binary = f.readlines()
        binary = b"".join(binary)

    filehash = utilities.hashMAC(hKey, binary)
    params = {
        "auth": authKey,
        "lastLogin": datetime.now().strftime('%d %b %Y, %I:%M %p'),
        "filehash": filehash
    }
    response = requests.post(url, json=params, headers={'content-type': 'application/json'})
    root.destroy()

class MainApplication(tk.Frame):
    def __init__(self, parent, login, lastLogin, vaultKey, username, auth, hmacKey):
        super().__init__()
        self.lastLogin = lastLogin
        # self.firebase = firebase
        self.login = login
        self.vaultKey = vaultKey
        self.username = username
        self.hmacKey = hmacKey
        global user
        user = self.username
        global root
        root = parent
        global authKey
        authKey = auth
        global hKey
        hKey = hmacKey

        self.database = DataBase(f"./{self.username}/{self.username}.db")
        self.credentials = self.database.fetchAllLogin(vaultKey)
        self.vault = self.database.fetchAllVault()
        self.notes = self.database.fetchAllNotes()
        self.items = {"login": self.credentials,
                      "notes": self.notes,
                      "vault": self.vault}

        self.parent = parent
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)

        self.servicesFrame = servicesFrame(parent, self, self.items, self.lastLogin)
        self.servicesFrame.grid(row=0, column=0, rowspan=3, sticky='nsew')

        self.itemsFrame = itemsFrame(parent, self, self.credentials)
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')

        self.detailsFrame = defaultDetailsFrame(parent)
        self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

        parent.protocol("WM_DELETE_WINDOW", onClose)

    def renderEditFrame(self, type, key):
        self.detailsFrame.destroy()
        if type == "login":
            self.detailsFrame = passwordEditFrame(self.parent, self, self.credentials[key], self.itemsFrame, self.database, self.vaultKey)
            self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')
        elif type == "vault":
            self.detailsFrame = vaultEditFrame(self.parent, self, self.vault[key], self.itemsFrame, self.database)
            self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')
        else:
            self.detailsFrame = notesEditFrame(self.parent, self, self.notes[key], self.itemsFrame, self.database, self.vaultKey, self.hmacKey)
            self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')
        #self.passwordGenerator = passwordGeneratorFrame(self.parent)
        #self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def reRenderDetailsFrame(self, json, type):
        self.detailsFrame.destroy()
        if type == "login":
            self.credentials[json['key']] = json
            self.items["login"][json['key']] = json
        elif type == "vault":
            self.vault[json['key']] = json
            self.items["vault"][json['key']] = json
        else:
            self.notes[json['key']] = json
            self.items["notes"][json['key']] = json
        self.changeDetailsFrame(json['key'])

    def updateItems(self, key, type):
        if type == "login":
            del self.credentials[key]
        elif type == "vault":
            del self.vault[key]
        else:
            del self.notes[key]
        self.changeItemsFrame(type)

    def displayDefaultFrame(self):
        self.detailsFrame.destroy()
        self.detailsFrame = defaultDetailsFrame(self.parent)
        self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')

        #self.passwordGenerator.destroy()
        #self.passwordGenerator = passwordGeneratorFrame(self.parent)
        #self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeDetailsFrame(self, key):
        self.detailsFrame.destroy()
        if key in self.credentials:
            self.detailsFrame = passwordDetailsFrame(self.parent, self, self.credentials[key], self.itemsFrame, self.database, self.vaultKey)
        elif key in self.vault:
            self.detailsFrame = vaultDetailsFrame(self.parent, self, self.vault[key], self.itemsFrame, self.database, self.vaultKey, self.hmacKey)
        else:
            self.detailsFrame = notesDetailsFrame(self.parent, self, self.notes[key], self.itemsFrame, self.database, self.vaultKey, self.hmacKey)
        self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')

        #self.passwordGenerator.destroy()
        #self.passwordGenerator = passwordGeneratorFrame(self.parent)
        #self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeItemsFrame(self, key, default=True):
        self.itemsFrame.destroyButtons()
        self.itemsFrame.destroy()
        self.itemsFrame = itemsFrame(self.parent, self, self.items[key])
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')
        if default:
            self.displayDefaultFrame()

    def changeCreateFrame(self, key):
        self.detailsFrame.destroy()
        if key == "notes":
            self.detailsFrame = notesCreateFrame(self.parent, self, self.database, self.vaultKey, self.username, self.hmacKey)
        elif key == "login":
            self.detailsFrame = passwordCreateFrame(self.parent, self, self.database, self.vaultKey)
        elif key == "vault":
            self.detailsFrame = vaultCreateFrame(self.parent, self, self.database, self.vaultKey, self.username, self.hmacKey)

        self.detailsFrame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.itemsFrame.destroy()
        self.changeItemsFrame(key, False)
        # self.itemsFrame.grid(row=0, column=1, rowspan=3, sticky='nsew')

    def logout(self):
        self.detailsFrame.destroy()
        self.itemsFrame.destroy()
        self.servicesFrame.destroy()
        self.passwordGenerator.destroy()
        onClose()
        self.login.loginPage()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    from util.firebase import Firebase
    base = Firebase()
    login = ""
    lastLogin = "23 Oct 2022"
    vaultkey = ""
    MainApplication(root, login, lastLogin, base, vaultkey).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
