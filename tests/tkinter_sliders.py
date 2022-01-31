from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')
root.geometry("400x400")

vertical = Scale(root, from_=400, to=800)
vertical.pack()

horizontal = Scale(root, from_=400, to=800, orient=HORIZONTAL)
horizontal.pack()

def slide():
	my_label=Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

my_label=Label(root, text=horizontal.get()).pack()



my_button = Button(root, text="Click me", command=slide).pack()

root.mainloop()