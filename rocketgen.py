from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
import os

root = Tk()
root.title('RocketGen')
root.iconbitmap('icon.ico')
style = ttk.Style(root)
root.tk.call('lappend', 'auto_path', 'awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')
style.theme_use('awdark')
my_img = ImageTk.PhotoImage(Image.open("RocketGenBanner.png"))



def select_file():

	# Get current working directory (cwd)
	cwd = os.getcwd()

	# Open a file dialog and store the selected filename in root.filename
	root.filename = filedialog.askopenfilename(initialdir=cwd+"/inputs", title="Select a file", filetypes=((".csv files", "*.csv"),("all files","*.*")))

	fileinput_entry.insert(0, root.filename)

	print(root.filename)

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
# Buttons
selectfile_button = ttk.Button(my_frame1, text="Select File", command=select_file)
#importfile_button = ttk.Button(my_frame1, text="Select File", command=select_file)
fileinput_entry = ttk.Entry(my_frame1, width=75)

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
fileinput_entry.grid(row=0, column=0)
selectfile_button.grid(row=0, column=1)

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
