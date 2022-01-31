from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Simple Calculator')

def show_info():
	response = messagebox.showinfo("Showinfo", "Info goes here")
	if response == "ok":
		Label(root, text="You clicked ok ('ok')").pack()

def show_warning():
	response = messagebox.showwarning("Showwarning", "Warning goes here")
	if response == "ok":
		Label(root, text="You clicked ok ('ok')").pack()

def show_error():
	response = messagebox.showerror("Showerror", "Error goes here")
	if response == "ok":
		Label(root, text="You clicked ok ('ok')").pack()

def ask_question():
	response = messagebox.askquestion("Askquestion", "Question goes here")
	if response == "yes":
		Label(root, text="You clicked yes ('yes')").pack()
	elif response == "no":
		Label(root, text="You clicked no ('no')").pack()

def ask_okcancel():
	response = messagebox.askokcancel("Askokcancel", "Question goes here")
	if response == 1:
		Label(root, text="You clicked ok (1)").pack()
	elif response == 0:
		Label(root, text="You clicked cancel (0)").pack()

def ask_yesno():
	response = messagebox.askyesno("Askyesno", "Question goes here")
	if response == 1:
		Label(root, text="You clicked yes (1)").pack()
	elif response == 0:
		Label(root, text="You clicked no (0)").pack()


Button(root, text="showinfo", command=show_info).pack()
Button(root, text="showwarning", command=show_warning).pack()
Button(root, text="showerror", command=show_error).pack()
Button(root, text="askquestion", command=ask_question).pack()
Button(root, text="askokcancel", command=ask_okcancel).pack()
Button(root, text="askyesno", command=ask_yesno).pack()


root.mainloop()