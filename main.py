from passwordGeneratorFrame import passwordGeneratorFrame
import tkinter as tk
class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.rowconfigure(2, weight=1)
        self.columnconfigure(5, weight=1)
        self.passwordGenerator = passwordGeneratorFrame(parent)
        self.passwordGenerator.grid(row=1, column=3, columnspan=2, sticky='ew')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Vault")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    MainApplication(root).grid(sticky='w')#side="top", fill="both", expand=True)
    root.mainloop()
