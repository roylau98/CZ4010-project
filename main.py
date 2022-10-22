from passwordGeneratorFrame import passwordGeneratorFrame
from detailsFrame import detailsFrame
from servicesFrame import servicesFrame
from itemsFrame import itemsFrame
import tkinter as tk
class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)

        self.servicesFrame = servicesFrame()
        self.servicesFrame.grid(row=0, column=0, rowspan=3, sticky='nsew', ipadx=80)
        self.itemsFrame = itemsFrame()
        self.itemsFrame.grid(row=0, column=1, rowspan=3,sticky='nsew')
        self.detailsFrame = detailsFrame(parent, {'account': 'Reddit', 'username': 'ABCD', 'password': '1234'})
        self.detailsFrame.grid(row=1, column=2, rowspan=2, columnspan=3, sticky='nsew')
        self.passwordGenerator = passwordGeneratorFrame(parent)
        self.passwordGenerator.grid(row=2, column=2, columnspan=3, sticky='nsew')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    MainApplication(root).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
