import tkinter as tk

class itemsFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)

        self.serviceLabelText = tk.StringVar()
        self.serviceLabelText.set("Services")
        self.serviceLabel = tk.Label(self, textvariable=self.serviceLabelText)

        self.serviceLabel.grid(row=0, column=0)