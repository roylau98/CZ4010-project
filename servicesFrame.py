import tkinter as tk

class servicesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(1, weight=1)

        self.serviceLabelText = tk.StringVar()
        self.serviceLabelText.set("Types")
        self.serviceLabel = tk.Label(self, textvariable=self.serviceLabelText)

        self.loginButton = tk.Button(self, text="Login")
        self.vaultButton = tk.Button(self, text="Vault")
        self.notesButton = tk.Button(self, text="Notes")

        self.serviceLabel.grid(row=0, column=0)
        self.loginButton.grid(row=1, column=0, sticky='nsew', ipadx=80)
        self.vaultButton.grid(row=2, column=0, sticky='nsew', ipadx=80)
        self.notesButton.grid(row=3, column=0, sticky='nsew', ipadx=80)