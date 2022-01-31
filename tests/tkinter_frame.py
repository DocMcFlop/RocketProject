from tkinter import *

root = Tk()
root.title('Simple Calculator')

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.pack()

root.mainloop()

