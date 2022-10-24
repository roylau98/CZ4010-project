from passwordGeneratorFrame import passwordGeneratorFrame
from detailsframe.passwordDetailsFrame import passwordDetailsFrame
from detailsframe.notesDetailsFrame import notesDetailsFrame
from detailsframe.defaultDetailsFrame import defaultDetailsFrame
from detailsframe.vaultDetailsFrame import vaultDetailsFrame
from editframe.passwordEditFrame import passwordEditFrame
from editframe.vaultEditFrame import vaultEditFrame
from editframe.notesEditFrame import notesEditFrame
from servicesFrame import servicesFrame
from itemsFrame import itemsFrame
import tkinter as tk
import json

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        with open('items.json', 'r') as f:
            self.items = json.load(f)
        self.credentials = self.items['login']
        self.vault = self.items['vault']
        self.notes = self.items['notes']

        self.parent = parent
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)

        self.servicesFrame = servicesFrame(parent, self, self.items)
        self.servicesFrame.grid(row=0, column=0, rowspan=3, sticky='nsew')

        self.itemsFrame = itemsFrame(parent, self, self.credentials)
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')

        self.detailsFrame = defaultDetailsFrame(parent)
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def renderEditFrame(self, type, key):
        if type == "login":
            self.detailsFrame = passwordEditFrame(self.parent, self, self.credentials[key], self.itemsFrame)
            self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        elif type == "vault":
            self.detailsFrame = vaultEditFrame(self.parent, self, self.vault[key], self.itemsFrame)
            self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        else:
            self.detailsFrame = notesEditFrame(self.parent, self, self.notes[key], self.itemsFrame)
            self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def reRenderDetailsFrame(self, json, type):
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
    def displayDefaultFrame(self):
        self.detailsFrame.destroy()
        self.detailsFrame = defaultDetailsFrame(self.parent)
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator.destroy()
        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeDetailsFrame(self, key):
        self.detailsFrame.destroy()
        if key in self.credentials:
            self.detailsFrame = passwordDetailsFrame(self.parent, self, self.credentials[key], self.itemsFrame)
        elif key in self.vault:
            self.detailsFrame = vaultDetailsFrame(self.parent, self, self.vault[key], self.itemsFrame)
        else:
            self.detailsFrame = notesDetailsFrame(self.parent, self, self.notes[key], self.itemsFrame)
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator.destroy()
        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeItemsFrame(self, key):
        self.itemsFrame.destroy()
        self.itemsFrame = itemsFrame(self.parent, self, self.items[key])
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')
        self.displayDefaultFrame()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    MainApplication(root).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
