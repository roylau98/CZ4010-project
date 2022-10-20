import tkinter as tk
from Crypto.Cipher import AES
import secrets
import utilities

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #<create the rest of your GUI here>
        #self.l1 = tk.Label(root, text="hello")
        #self.l2 = tk.Label(root, text="world")
        #self.l1.grid(row=0, column=0)
        #self.l2.grid(row=0, column=1)


        self.passwordGenerator = tk.Frame(self.parent)
        self.b1 = tk.Button(self.passwordGenerator, text="Generate", command=utilities.passwordGenerator())
        self.output = tk.Text(self.passwordGenerator, height=1, width=52)
        # self.passwordGenerator.grid(row=1, column=2, sticky="sw")
        self.b1.grid(row=0, column=0)
        self.output.grid(row=0, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
