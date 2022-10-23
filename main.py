from passwordGeneratorFrame import passwordGeneratorFrame
from passwordDetailsFrame import passwordDetailsFrame
from servicesFrame import servicesFrame
from itemsFrame import itemsFrame
import tkinter as tk
import json

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        with open('login.json', 'r') as f:
            self.credentials = json.load(f)

        with open('vault.json', 'r') as f:
            self.vault = json.load(f)

        with open('notes.json', 'r') as f:
            self.notes = json.load(f)

        self.parent = parent
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)

        self.servicesFrame = servicesFrame(parent)
        self.servicesFrame.grid(row=0, column=0, rowspan=3, sticky='nsew')
        self.itemsFrame = itemsFrame(parent, self, self.credentials)
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')
        self.detailsFrame = passwordDetailsFrame(parent, self.credentials[list(self.credentials)[0]])
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        self.passwordGenerator = passwordGeneratorFrame(parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

    def changeDetailsFrame(self, key):
        self.detailsFrame.destroy()
        self.detailsFrame = passwordDetailsFrame(self.parent, self.credentials[key])
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='new')

    def changeItemsFrame(self, key):
        self.itemsFrame.destroy()
        self.detailsFrame = detailsFrame(self.parent, self.credentials[key])
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='new')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    MainApplication(root).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
