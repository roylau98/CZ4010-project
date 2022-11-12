import tkinter as tk
from datetime import datetime

class itemsFrame(tk.Frame):
    def __init__(self, parent, main, items):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.current = datetime.now()

        self.main = main
        self.button = []
        i = 0
        for key in items:
            if "account" in items[key]:
                self.button.append(tk.Button(self, text=items[key]['account'] + "\n" + items[key]['username'], command=lambda key=key: self.changeDetails(key), anchor='w'))
                formattedDate = datetime.strptime(items[key]['updated'], '%d %b %Y, %I:%M %p')
                difference = (self.current.year - formattedDate.year) * 12 + (self.current.month - formattedDate.month)
                if difference >= 3:
                    self.button[i].config(fg="red")
            elif "title" in items[key]:
                self.button.append(
                    tk.Button(self, text=items[key]['title'].strip() + '\n' + items[key]['path'].strip() + "/" +
                                         items[key]['filename'].strip(), command=lambda key=key: self.changeDetails(key), anchor='w'))
            self.button[i].grid(row=i+1, column=0, sticky='nsew', ipadx=175)
            i += 1

    def changeDetails(self, key):
        self.main.changeDetailsFrame(key)

    def deleteButton(self, key):
        for i in range(len(self.button)):
            if self.button[i]['text'] == key:
                break
        self.button[i].destroy()
        del self.button[i]

    def updateItems(self, key, newKey):
        for i in range(len(self.button)):
            if self.button[i]['text'] == key:
                break
        self.button[i].config(text=newKey.strip())

    def destroyButtons(self):
        for i in range(len(self.button)):
            self.button[i].destroy()