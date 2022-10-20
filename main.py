import string
import tkinter as tk
from Crypto.Cipher import AES
import secrets
import utilities

class passwordGeneratorFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, text="Generate", command=self.generatePassword)
        self.copy = tk.Button(self, text="Copy", command=self.copyToClipboard)
        self.output = tk.Text(self, height=1, width=60)

        self.punctuation = tk.IntVar()
        self.digits = tk.IntVar()
        self.uppercase = tk.IntVar()
        self.scaleBarOutput = tk.Text(self, height=1, width=3)
        self.scaleBarOutput.insert("end", "8")
        self.scaleBar = tk.Scale(self, from_=8, to=60, orient="horizontal", command=self.updateScaleText)
        self.checkBoxP = tk.Checkbutton(self, text="Punctuation", variable=self.punctuation)
        self.checkBoxD = tk.Checkbutton(self, text="Digits", variable=self.digits)
        self.checkBoxU = tk.Checkbutton(self, text="Uppercase", variable=self.uppercase)

        self.button.grid(row=0, column=0)
        self.output.grid(row=0, column=1)
        self.copy.grid(row=0, column=2)
        self.checkBoxP.grid(row=1, column=0)
        self.checkBoxD.grid(row=1, column=1)
        self.checkBoxU.grid(row=1, column=2)
        self.scaleBar.grid(row=2, column=1)
        self.scaleBarOutput.grid(row=2, column=0)
    def generatePassword(self):
        pool = string.ascii_lowercase
        if self.punctuation.get():
            pool += string.punctuation
        if self.digits.get():
            pool += string.digits
        if self.uppercase.get():
            pool += string.ascii_uppercase

        password = utilities.passwordGenerator(pool, self.scaleBar.get())
        self.output.delete(1.0, "end")
        self.output.insert("end", password)
        return password

    def updateScaleText(self, val):
        self.scaleBarOutput.delete(1.0, "end")
        self.scaleBarOutput.insert("end", val)

    def copyToClipboard(self):
        super().clipboard_append(self.output.get("end"))

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.passwordGenerator = passwordGeneratorFrame()
        self.passwordGenerator.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
