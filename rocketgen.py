from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle

root = Tk()
root.title('RocketGen')
root.iconbitmap('icon.ico')
style = ttk.Style(root)
root.tk.call('lappend', 'auto_path', 'awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')
style.theme_use('awdark')
my_img = ImageTk.PhotoImage(Image.open("RocketGenBanner.png"))

# Notebooks
my_notebook = ttk.Notebook(root)
# Labels
program_banner = ttk.Label(image=my_img)
# Frames
my_frame1 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame2 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame3 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame4 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame5 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame6 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame7 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame8 = ttk.Frame(my_notebook, width=1080, height=720)

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
my_frame8.pack(fill="both", expand=1)

# Add frames to notebook as tabs
my_notebook.add(my_frame1, text="Inputs")
my_notebook.add(my_frame2, text="Output Summary")
my_notebook.add(my_frame3, text="Performance")
my_notebook.add(my_frame4, text="Geometry")
my_notebook.add(my_frame5, text="Injector")
my_notebook.add(my_frame6, text="Heat Transfer")
my_notebook.add(my_frame7, text="Stress Analysis")
my_notebook.add(my_frame8, text="CEA Evaluation")



root.mainloop()
