import tkinter as tk
import json

class registerFrame(tk.Frame):
    def __init__(self, parent, login):
        super().__init__()
        self.parent = parent
        self.rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.font = ('Times', 14)
        self.login = login

        self.variable = tk.StringVar()
        self.right_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)
        self.usernameLabel = tk.Label(self, text="Enter Username", bg='#CCCCCC', font=self.font)
        self.emailLabel = tk.Label(self, text="Enter Email", bg='#CCCCCC', font=self.font)
        self.passwordLabel = tk.Label(self,text="Enter Password", bg='#CCCCCC', font=self.font)
        self.rePasswordLabel = tk.Label(self,text="Re-Enter Password", bg='#CCCCCC', font=self.font)

        self.register_username = tk.Entry(self, font=self.font)
        self.register_email = tk.Entry(self, font=self.font)
        self.register_pwd = tk.Entry(self, font=self.font, show='*')
        self.pwd_again = tk.Entry(self, font=self.font, show='*')
        self.register_btn = tk.Button(self, width=15, text='Register', font=self.font, relief=tk.SOLID, cursor='hand2', command=self.registerUser)
        self.return_btn = tk.Button(self, width=15, text='Return', font=self.font, relief=tk.SOLID, cursor='hand2',
                                      command=self.returnLogin)

        self.usernameLabel.grid(row=0, column=0, pady=10, padx=20)
        self.emailLabel.grid(row=1, column=0, pady=10, padx=20)
        self.passwordLabel.grid(row=5, column=0, pady=10, padx=20)
        self.rePasswordLabel.grid(row=6, column=0, pady=10, padx=20)
        self.register_username.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=6, column=1, pady=10, padx=20)
        self.register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.return_btn.grid(row=7, column=0, pady=10, padx=20)

    def registerUser(self):
        pass

    def returnLogin(self):
        self.grid_forget()
        self.login.loginPage()