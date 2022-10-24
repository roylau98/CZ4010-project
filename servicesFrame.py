import tkinter as tk

class servicesFrame(tk.Frame):
    def __init__(self, parent, main, items):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.main = main
        self.items = list(items)
        self.serviceLabelText = tk.StringVar()
        self.serviceLabelText.set("Types")
        self.serviceLabel = tk.Label(self, textvariable=self.serviceLabelText)

        self.serviceLabel.grid(row=0, column=0, pady=30)
        self.main = main
        self.button = []
        i = 0
        for item in self.items:
            self.button.append(
                tk.Button(self, text=item.title(), command=lambda item=item: self.changeItems(item)))
            self.button[i].grid(row=i + 1, column=0, sticky='nsew', ipadx=80)
            i += 1

    def changeItems(self, item):
        print(item)
        self.main.changeItemsFrame(item)