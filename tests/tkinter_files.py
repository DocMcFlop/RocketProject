from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')

def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="/tests", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image=my_image).pack()

my_button = Button(root, text="Open file", command=open).pack()

root.mainloop()