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

        # self.loginButton = tk.Button(self, text="Login")
        # self.vaultButton = tk.Button(self, text="Vault")
        # self.notesButton = tk.Button(self, text="Notes")

        self.serviceLabel.grid(row=0, column=0)
        # self.loginButton.grid(row=1, column=0, sticky='nsew', ipadx=80)
        # self.vaultButton.grid(row=2, column=0, sticky='nsew', ipadx=80)
        # self.notesButton.grid(row=3, column=0, sticky='nsew', ipadx=80)

        self.main = main
        self.button = []
        i = 0
        for item in self.items:
            self.button.append(
                tk.Button(self, text=item.title(), command=lambda item=item: self.changeItems(item)))
            self.button[i].grid(row=i + 1, column=0, sticky='nsew', ipadx=80)
            i += 1
        print(len(self.button))

    def changeItems(self, item):
        self.main.changeItemsFrame(item)