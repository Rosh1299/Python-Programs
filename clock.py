from tkinter import *
from tkinter.ttk import *
from time import *

root = Tk()
root.title("Digital Clock")


def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=('Arial', 125),
              background="black", foreground="white")
label.pack(anchor="center")
time()
mainloop()
