from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Weiner weiner weiner")
    myLabel.pack()


myButton = Button(root, text="Button button", command=myClick)
myButton.pack()

root.mainloop()

