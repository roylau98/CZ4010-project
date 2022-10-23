from passwordGeneratorFrame import passwordGeneratorFrame
from passwordDetailsFrame import passwordDetailsFrame
from notesDetailsFrame import notesDetailsFrame
from defaultDetailsFrame import defaultDetailsFrame
from vaultDetailsFrame import vaultDetailsFrame
from servicesFrame import servicesFrame
from loginItemsFrame import loginItemsFrame
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

        self.servicesFrame = servicesFrame(parent)
        self.servicesFrame.grid(row=0, column=0, rowspan=3, sticky='nsew')
        self.itemsFrame = loginItemsFrame(parent, self, self.credentials)
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')
        #self.detailsFrame = passwordDetailsFrame(parent, self, self.credentials[list(self.credentials)[0]])
        #self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        #self.detailsFrame = notesDetailsFrame(parent, self, self.notes[list(self.notes)[0]])
        #self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        # self.detailsFrame = defaultDetailsFrame(parent)
        # self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.detailsFrame = vaultDetailsFrame(parent, self, self.vault[list(self.vault)[0]])
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        self.passwordGenerator = passwordGeneratorFrame(parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def displayDefaultFrame(self):
        self.detailsFrame.destroy()
        self.detailsFrame = defaultDetailsFrame(self.parent)
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator.destroy()
        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeDetailsFrame(self, key):
        self.detailsFrame.destroy()
        self.detailsFrame = passwordDetailsFrame(self.parent, self, self.credentials[key])
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')

        self.passwordGenerator.destroy()
        self.passwordGenerator = passwordGeneratorFrame(self.parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeItemsFrame(self, key):
        self.itemsFrame.destroy()
        self.itemsFrame = loginItemsFrame(parent, self, self.credentials)
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    MainApplication(root).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
