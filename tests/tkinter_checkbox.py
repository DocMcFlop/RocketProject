from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')
root.geometry("400x400")

var = StringVar()

checkbox = Checkbutton(root, text="Check this box, I dare you", variable=var, onvalue="On", offvalue="Off")
checkbox.deselect()
checkbox.pack()

def show():
	my_label = Label(root, text=var.get()).pack()

my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()