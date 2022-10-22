import threading
import tkinter as tk
import string
import time
import utilities

class passwordGeneratorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.rowconfigure(8, weight=1)
        self.columnconfigure(4, weight=1)
        self.parent = parent
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1)

        self.passwordGeneratorText = tk.StringVar()
        self.passwordGeneratorText.set("Generator: ")
        self.passwordGeneratorLabel = tk.Label(self, textvariable=self.passwordGeneratorText)
        self.button = tk.Button(self, text="Generate", command=self.generatePassword)
        self.copy = tk.Button(self, text="Copy", command=self.copyToClipboard)
        self.clear = tk.Button(self, text="Clear", command=self.clearOutput)
        self.output = tk.Text(self, height=1, width=60)

        self.scaleBarLabelText = tk.StringVar()
        self.scaleBarLabelText.set("Length")
        self.scaleBarLabel = tk.Label(self, textvariable=self.scaleBarLabelText)
        self.scaleBarOutput = tk.Text(self, height=1, width=3)
        self.scaleBarOutput.insert("end", "24")
        self.scaleBar = tk.Scale(self, from_=8, to=60, orient="horizontal", command=self.updateScaleText, showvalue=0)
        self.scaleBar.set(24)

        self.punctuation = tk.IntVar()
        self.checkBoxPText = tk.StringVar()
        self.checkBoxPText.set("Punctuation")
        self.checkBoxPLabel = tk.Label(self, textvariable=self.checkBoxPText)
        self.checkBoxP = tk.Checkbutton(self, variable=self.punctuation, command=self.tickCheckBox)
        self.checkBoxP.select()

        self.digits = tk.IntVar()
        self.checkBoxDText = tk.StringVar()
        self.checkBoxDText.set("Digits")
        self.checkBoxDLabel = tk.Label(self, textvariable=self.checkBoxDText)
        self.checkBoxD = tk.Checkbutton(self, variable=self.digits, command=self.tickCheckBox)
        self.checkBoxD.select()

        self.uppercase = tk.IntVar()
        self.checkBoxUText = tk.StringVar()
        self.checkBoxUText.set("Uppercase")
        self.checkBoxULabel = tk.Label(self, textvariable=self.checkBoxUText)
        self.checkBoxU = tk.Checkbutton(self, variable=self.uppercase, command=self.tickCheckBox)
        self.checkBoxU.select()

        self.lowercase = tk.IntVar()
        self.checkBoxLText = tk.StringVar()
        self.checkBoxLText.set("Lowercase")
        self.checkBoxLLabel = tk.Label(self, textvariable=self.checkBoxLText)
        self.checkBoxL = tk.Checkbutton(self, variable=self.lowercase, command=self.tickCheckBox)
        self.checkBoxL.select()

        self.passwordGeneratorLabel.grid(row=0, column=0, padx=5, pady=5)
        self.output.grid(row=1, column=1, padx=5, pady=5)
        self.button.grid(row=1, column=0, padx=5, pady=5)
        self.copy.grid(row=1, column=2, padx=5, pady=5)
        self.clear.grid(row=1, column=3, padx=5, pady=5)
        self.scaleBarLabel.grid(row=3, column=0, padx=5, pady=5)
        self.scaleBarOutput.grid(row=3, column=2, padx=5)
        self.scaleBar.grid(row=3, column=1, sticky='ew')

        self.checkBoxLLabel.grid(row=4, column=0)
        self.checkBoxL.grid(row=4, column=2, padx=5)
        self.checkBoxULabel.grid(row=5, column=0)
        self.checkBoxU.grid(row=5, column=2, padx=5)
        self.checkBoxDLabel.grid(row=6, column=0)
        self.checkBoxD.grid(row=6, column=2, padx=5)
        self.checkBoxPLabel.grid(row=7, column=0)
        self.checkBoxP.grid(row=7, column=2, padx=5)

    def generatePassword(self):
        pool = ""
        if self.lowercase.get():
            pool += string.ascii_lowercase
        if self.punctuation.get():
            pool += string.punctuation
        if self.digits.get():
            pool += string.digits
        if self.uppercase.get():
            pool += string.ascii_uppercase

        password = utilities.passwordGenerator(pool, self.scaleBar.get())
        self.output.delete(1.0, "end")
        self.output.insert("end", password)

        background = threading.Thread(target=self.clearOutputBackground, daemon=True)
        background.start()
        return password

    def updateScaleText(self, val):
        self.scaleBarOutput.delete(1.0, "end")
        self.scaleBarOutput.insert("end", val)

    def tickCheckBox(self):
        checked = self.uppercase.get() or self.lowercase.get() or self.digits.get() or self.punctuation.get()

        if not checked:
            self.checkBoxU.select()

    def copyToClipboard(self):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(self.output.get("1.0", "end")[:-1])
        background = threading.Thread(target=self.clearClipboard, daemon=True)
        background.start()

    def clearClipboard(self):
        time.sleep(10)
        print("Cleared clipboard")
        self.parent.clipboard_clear()
        self.parent.clipboard_append('')

    def clearOutputBackground(self):
        time.sleep(10)
        print("Cleared output")
        self.output.delete(1.0, "end")

    def clearOutput(self):
        self.output.delete(1.0, "end")