import tkinter as tk

class itemsFrame(tk.Frame):
    def __init__(self, parent, main, items):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)

        self.main = main
        self.button = []
        i = 0
        for key in items:
            if "account" in items[key]:
                self.button.append(tk.Button(self, text=items[key]['account'], command=lambda key=key: self.changeDetails(key)))
            elif "title" in items[key]:
                self.button.append(
                    tk.Button(self, text=items[key]['title'], command=lambda key=key: self.changeDetails(key)))
            self.button[i].grid(row=i+1, column=0, sticky='nsew', ipadx=178)
            i += 1

    def changeDetails(self, key):
        self.main.changeDetailsFrame(key)
