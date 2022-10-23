import tkinter as tk

class itemsFrame(tk.Frame):
    def __init__(self, parent, main, credentials):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)

        self.main = main
        self.button = []
        i = 0
        for key in credentials:
            self.button.append(tk.Button(self, text=credentials[key]['account'], command=lambda key=key: self.changeDetails(key)))
            self.button[i].grid(row=i+1, column=0, sticky='nsew', ipadx=172)
            i += 1
        print(len(self.button))

    def changeDetails(self, key):
        self.main.changeDetailsFrame(key)
