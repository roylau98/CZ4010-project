from tkinter import *


ws = Tk()
ws.title('Registration')
ws.config(bg='#0B5A81')

f = ('Times', 14)

variable = StringVar()

right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )


Label(
    right_frame, 
    text="Enter Username", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10, 
    pady=10,
    )


register_username = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None
)


register_username.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()

ws.mainloop()