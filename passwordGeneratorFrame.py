import threading
import tkinter as tk
import string
import time
import utilities

class passwordGeneratorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.rowconfigure(14, weight=1)
        self.columnconfigure(3, weight=1)
        self.parent = parent
        tk.Frame.__init__(self, highlightbackground='black', highlightthickness=1, height=360)

        self.button = tk.Button(self, text="Generate", command=self.generatePassword)
        self.copy = tk.Button(self, text="Copy", command=self.copyToClipboard)
        self.output = tk.Text(self, height=1, width=50)

        self.scaleBarLabelText = tk.StringVar()
        self.scaleBarLabelText.set("Length")
        self.scaleBarLabel = tk.Label(self, textvariable=self.scaleBarLabelText)
        self.scaleBarOutput = tk.Text(self, height=1, width=3)
        self.scaleBarOutput.insert("end", "24")
        self.scaleBar = tk.Scale(self, from_=8, to=50, orient="horizontal", command=self.updateScaleText, showvalue=0)
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

        self.button.grid(row=0, column=0)
        self.output.grid(row=0, column=1, columnspan=2, sticky='w')
        self.copy.grid(row=2, column=0)
        self.scaleBarLabel.grid(row=4, column=0)
        self.scaleBarOutput.grid(row=4, column=1)
        self.scaleBar.grid(row=4, column=2, sticky='ew')

        self.checkBoxLLabel.grid(row=7, column=0)
        self.checkBoxL.grid(row=7, column=2)
        self.checkBoxULabel.grid(row=9, column=0)
        self.checkBoxU.grid(row=9, column=2)
        self.checkBoxDLabel.grid(row=11, column=0)
        self.checkBoxD.grid(row=11, column=2)
        self.checkBoxPLabel.grid(row=13, column=0)
        self.checkBoxP.grid(row=13, column=2)

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
        self.parent.clipboard_append(self.output.get("1.0", "end"))
        background = threading.Thread(target=self.clearClipboard, daemon=True)
        background.start()

    def clearClipboard(self):
        time.sleep(10)
        print("Cleared clipboard")
        self.parent.clipboard_clear()
        self.parent.clipboard_append('')