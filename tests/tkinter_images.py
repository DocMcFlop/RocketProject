from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle

root = Tk()
root.title('RocketGen')
root.iconbitmap('icon.ico')
style = ThemedStyle(root)
style.set_theme("scidgrey")
my_img = ImageTk.PhotoImage(Image.open("RocketGenBanner.png"))

# Notebooks
my_notebook = ttk.Notebook(root)
# Labels
program_banner = Label(image=my_img, borderwidth=5)
# Frames
my_frame1 = Frame(my_notebook, width=1080, height=720)
my_frame2 = Frame(my_notebook, width=1080, height=720)
my_frame3 = Frame(my_notebook, width=1080, height=720)
my_frame4 = Frame(my_notebook, width=1080, height=720)
my_frame5 = Frame(my_notebook, width=1080, height=720)
my_frame6 = Frame(my_notebook, width=1080, height=720)
my_frame7 = Frame(my_notebook, width=1080, height=720)

# Pack widgets
program_banner.grid(row=0, column=0)
my_notebook.grid(row=1, column=0)
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)
my_frame4.pack(fill="both", expand=1)
my_frame5.pack(fill="both", expand=1)
my_frame6.pack(fill="both", expand=1)
my_frame7.pack(fill="both", expand=1)

# Add frames to notebook as tabs
my_notebook.add(my_frame1, text="Inputs")
my_notebook.add(my_frame2, text="Output Summary")
my_notebook.add(my_frame3, text="Performance")
my_notebook.add(my_frame4, text="Geometry")
my_notebook.add(my_frame5, text="Injector")
my_notebook.add(my_frame6, text="Heat Transfer")
my_notebook.add(my_frame7, text="Stress Analysis")






root.mainloop()
