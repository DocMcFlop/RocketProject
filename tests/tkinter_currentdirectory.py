from tkinter import *
import os

root = Tk()
root.title('Simple Calculator')

cwd = os.getcwd()
my_label = Label(root, text=cwd)
my_label.pack()

root.mainloop()

