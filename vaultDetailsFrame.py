import tkinter as tk
import utilities


class vaultDetailsFrame(tk.Frame):
    def __init__(self, parent, json):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent
        self.rowconfigure(7, weight=1)
        self.columnconfigure(3, weight=1)

