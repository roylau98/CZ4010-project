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
                self.button.append(tk.Button(self, text=items[key]['account'] + "\n" + items[key]['username'], command=lambda key=key: self.changeDetails(key), anchor='w'))
            elif "title" in items[key]:
                self.button.append(
                    tk.Button(self, text=items[key]['title'] + '\n' + items[key]['path'] + "/" + items[key]['filename'], command=lambda key=key: self.changeDetails(key), anchor='w'))
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