import tkinter as tk

class defaultDetailsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.parent = parent