from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')

def open():
	global my_img
	top = Toplevel() #Syntax for a second window is Toplevel() instead of Tk()
	my_img = ImageTk.PhotoImage(Image.open("RocketGenBanner.png"))
	my_label = Label(top, image=my_img).pack()
	my_button2 = Button(top, text="Close window", command=top.destroy).pack()

my_button = Button(root, text="Open second window", command=open).pack()

root.mainloop()