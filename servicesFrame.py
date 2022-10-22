import tkinter as tk

class servicesFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(1, weight=1)

        self.serviceLabelText = tk.StringVar()
        self.serviceLabelText.set("Services")
        self.serviceLabel = tk.Label(self, textvariable=self.serviceLabelText)

        self.loginButton = tk.Button(self, text="Login")
        self.vaultButton = tk.Button(self, text="Vault")
        self.notesButton = tk.Button(self, text="Notes")

        self.serviceLabel.grid(row=0, column=0, ipadx=50, ipady=50)
        self.loginButton.grid(row=1, column=0)
        self.vaultButton.grid(row=2, column=0)
        self.notesButton.grid(row=3, column=0)