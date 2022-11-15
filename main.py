from utilframe.loginFrame import loginFrame
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("LastCrypt")
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    loginFrame(root).grid(row=1, column=1)  # side="top", fill="both", expand=True)
    # root.protocol("WM_DELETE_WINDOW", onClose)
    root.mainloop()

if __name__=='__main__':
    main()