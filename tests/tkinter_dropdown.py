from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')
root.geometry("400x400")

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
	]

var = StringVar()
var.set(options[0])

drop = OptionMenu(root, var, *options)
drop.pack()

def show():
	my_label = Label(root, text=var.get()).pack()

my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()