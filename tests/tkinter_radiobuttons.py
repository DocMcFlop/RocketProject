from tkinter import *

root = Tk()
root.title('Simple Calculator')

r = IntVar()
r.set("1")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ]

pizza = StringVar()
pizza.set("Pepperoni")

def clicked(value):
	my_label = Label(root, text=value)
	my_label.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

for text, mode in MODES:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

my_button = Button(root, text="click me", command=lambda: clicked(pizza.get()))
my_button.pack()

#my_label = Label(root, text=pizza.get())
#my_label.pack()

root.mainloop()