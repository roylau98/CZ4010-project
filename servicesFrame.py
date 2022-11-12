import tkinter as tk

class servicesFrame(tk.Frame):
    def __init__(self, parent, main, items, lastLogin):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.rowconfigure(8, weight=1)
        self.columnconfigure(1, weight=1)
        self.main = main
        self.items = list(items)
        self.serviceLabelText = tk.StringVar()
        self.serviceLabelText.set("Services")
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

        self.choices = ["                      Login                    ",
                        "                      Notes                    ",
                        "                      Vault                    "]
        self.choice = tk.StringVar()
        self.choice.set(self.choices[0])

        self.newLabelText = tk.StringVar()
        self.newLabelText.set("New Entry")
        self.newserviceLabel = tk.Label(self, textvariable=self.newLabelText)
        self.newserviceLabel.grid(row=i+1, column=0, pady=80, sticky='s')

        self.dropdownList = tk.OptionMenu(self, self.choice, *self.choices, command=self.createNew)
        self.dropdownList.config(width=30)
        self.dropdownList.grid(row=i+2, column=0, sticky='nsew')

        self.logout = tk.Button(self, text="Logout", command=self.logoutApp)
        self.logout.grid(row=7, column=0, sticky='sew', pady=100)
        self.lastLoginTimeText = tk.StringVar()
        self.lastLoginTimeText.set("Last Login: " + lastLogin)
        self.lastLoginTime = tk.Label(self, textvariable=self.lastLoginTimeText)
        self.lastLoginTime.config(fg="red")
        self.lastLoginTime.grid(row=8, column=0, sticky='sew')

    def changeItems(self, item):
        self.main.changeItemsFrame(item)

    def createNew(self, key):
        self.main.changeCreateFrame(key.strip())

    def logoutApp(self):
        self.main.logout()