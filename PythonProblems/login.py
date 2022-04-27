from tkinter import *
from tkinter import ttk

root = Tk()

L1 = Label(root, text = "Welcome", font=("Arial", 20))
L1.pack()

usernameLabel = Label(root, text = "Username:", font=("Arial", 14))
usernameLabel.pack(side = LEFT)

passwordLabel = Label(root, text = "Password:", font=("Arial", 14))
passwordLabel.pack(row=2, side = LEFT)

usernameEntry = Entry(root)
usernameEntry.pack(side = RIGHT)

root.mainloop()
