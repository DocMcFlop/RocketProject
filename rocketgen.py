from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
import os

# Tkinter window initialization
root = Tk()
root.title('RocketGen')
root.iconbitmap('icon.ico')
root.tk.call('lappend', 'auto_path', 'awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')
style = ttk.Style(root)
style.theme_use('awdark')
banner_img = ImageTk.PhotoImage(Image.open("RocketGenBanner.png"))

# User-selected variables
heattransfer_boolean = IntVar()
geometrygeneration_boolean = IntVar()
correctionfactors_boolean = IntVar()
stressanalysis_boolean = IntVar()
flowanalysis_boolean = IntVar()
injectoranalysis_boolean = IntVar()
defaultunits_selection = StringVar()
length_selection = StringVar()
area_selection = StringVar()
volume_selection = StringVar()
velocity_selection = StringVar()
pressure_selection = StringVar()
temperature_selection = StringVar()
force_selection = StringVar()
energy_selection = StringVar()
power_selection = StringVar()

# Function to open a file
def select_file():

	# Clear current entry
	fileinput_entry.delete(0, END)

	# Open a file dialog and store the selected filename in root.filename
	root.filename = filedialog.askopenfilename(initialdir=os.getcwd()+"/inputs",
	 title="Select a file", filetypes=((".csv files", "*.csv"),("all files","*.*")))

	# Insert filename into entry widget
	fileinput_entry.insert(0, root.filename)

def import_file():
	try:
		print(root.filename)
	except AttributeError:
		pass

def run():
	print("Filename: ", fileinput_entry.get())
	print("Heat Transfer: ", heattransfer_boolean.get())
	print("Geometry Generation: ", geometrygeneration_boolean.get())
	print("Correction Factors: ", correctionfactors_boolean.get())
	print("Stress Analysis: ", stressanalysis_boolean.get())
	print("Flow Analysis: ", flowanalysis_boolean.get())
	print("Injector Analysis: ", injectoranalysis_boolean.get())

# Units options
default_units = [
			"Metric",
			"Imperial"
			]
length_units = [
			"[m]",
			"[ft]",
			"[in]"
			]
area_units = [
			"[m^2]",
			"[ft^2]",
			"[in^2]"
			]
volume_units = [
			"[m^3]",
			"[ft^3]",
			"[in^3]"
			]
velocity_units = [
			"[m s^-1]",
			"[ft s^-1]",
			"[in s^-1]"
			]
pressure_units = [
			"[N m^-2]",
			"[lbf in^-2]"
			]
temperature_units = [
			"[K]",
			"[R]",
			"[C]",
			"[F]"
			]
force_units = [
			"[N]",
			"[lbf]"
			]
energy_units = [
			"[J]"
			]
power_units = [
			"[W]"
			]			

# Notebooks
my_notebook = ttk.Notebook(root)
# Frames
my_frame1 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame2 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame3 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame4 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame5 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame6 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame7 = ttk.Frame(my_notebook, width=1080, height=720)
my_frame8 = ttk.Frame(my_notebook, width=1080, height=720)
input_frame = ttk.Frame(my_frame1, width=1080, height=100, borderwidth=5, relief="groove")
leftinput_frame = ttk.Frame(input_frame, padding=2)
middleinput_frame = ttk.Frame(input_frame, padding=2)
rightinput_frame = ttk.Frame(input_frame, padding=2)
units_frame = ttk.Frame(my_frame1, width=200, height=200, borderwidth=5, relief="groove")
unitslabel_frame = ttk.Frame(units_frame, borderwidth=5, relief="groove")
# Labels
banner_label = ttk.Label(root, image=banner_img)
unitsframe_label = ttk.Label(unitslabel_frame, text="Units")
length_label = ttk.Label(units_frame, text="Length: ")
area_label = ttk.Label(units_frame, text="Area: ")
volume_label = ttk.Label(units_frame, text="Volume: ")
velocity_label = ttk.Label(units_frame, text="Velocity: ")
pressure_label = ttk.Label(units_frame, text="Pressure: ")
temperature_label = ttk.Label(units_frame, text="Temperature: ")
force_label = ttk.Label(units_frame, text="Force: ")
energy_label = ttk.Label(units_frame, text="Energy: ")
power_label = ttk.Label(units_frame, text="Power: ")
# Checkbuttons
# Buttons
selectfile_button = ttk.Button(leftinput_frame, text="Select File", command=select_file)
importfile_button = ttk.Button(leftinput_frame, text="Import", command=import_file)
run_button = ttk.Button(rightinput_frame, text="RUN", command=run)
# Entries
fileinput_entry = ttk.Entry(leftinput_frame, width=50)
# Optionmenus
defaultunits_optionmenu = ttk.OptionMenu(units_frame, defaultunits_selection, default_units[0], *default_units)
length_optionmenu = ttk.OptionMenu(units_frame, length_selection, length_units[0], *length_units)
area_optionmenu = ttk.OptionMenu(units_frame, area_selection, area_units[0], *area_units)
volume_optionmenu = ttk.OptionMenu(units_frame, volume_selection, volume_units[0], *volume_units)
velocity_optionmenu = ttk.OptionMenu(units_frame, velocity_selection, velocity_units[0], *velocity_units)
pressure_optionmenu = ttk.OptionMenu(units_frame, pressure_selection, pressure_units[0], *pressure_units)
temperature_optionmenu = ttk.OptionMenu(units_frame, temperature_selection, temperature_units[0], *temperature_units)
force_optionmenu = ttk.OptionMenu(units_frame, force_selection, force_units[0], *force_units)
energy_optionmenu = ttk.OptionMenu(units_frame, energy_selection, energy_units[0], *energy_units)
power_optionmenu = ttk.OptionMenu(units_frame, power_selection, power_units[0], *power_units)
# Checkbuttons
heattransfer_checkbox = ttk.Checkbutton(middleinput_frame, text="Heat transfer analysis", variable=heattransfer_boolean)
geometrygeneration_checkbox = ttk.Checkbutton(middleinput_frame, text="Geometry generation", variable=geometrygeneration_boolean)
correctionfactors_checkbox = ttk.Checkbutton(middleinput_frame, text="Correction factors", variable=correctionfactors_boolean)
stressanalysis_checkbox = ttk.Checkbutton(middleinput_frame, text="Stress analysis", variable=stressanalysis_boolean)
flowanalysis_checkbox = ttk.Checkbutton(middleinput_frame, text="Flow analysis", variable=flowanalysis_boolean)
injectoranalysis_checkbox = ttk.Checkbutton(middleinput_frame, text="Injector analysis", variable=injectoranalysis_boolean)

# Pack widgets
# Main window
banner_label.grid(row=0, column=0)
my_notebook.grid(row=1, column=0)
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)
my_frame4.pack(fill="both", expand=1)
my_frame5.pack(fill="both", expand=1)
my_frame6.pack(fill="both", expand=1)
my_frame7.pack(fill="both", expand=1)
my_frame8.pack(fill="both", expand=1)
# Input frame
input_frame.pack(fill="x")
leftinput_frame.grid(row=0, column=0)
middleinput_frame.grid(row=0, column=1)
rightinput_frame.grid(row=0, column=2)
fileinput_entry.grid(row=0, column=0, padx=2, pady=2)
selectfile_button.grid(row=0, column=1, padx=2, pady=2)
importfile_button.grid(row=0, column=2, padx=2, pady=2)
heattransfer_checkbox.grid(row=0, column=3, sticky="W")
geometrygeneration_checkbox.grid(row=0, column=4, sticky="W")
correctionfactors_checkbox.grid(row=0, column=5, sticky="W")
stressanalysis_checkbox.grid(row=1, column=3, sticky="W")
flowanalysis_checkbox.grid(row=1, column=4, sticky="W")
injectoranalysis_checkbox.grid(row=1, column=5, sticky="W")
run_button.grid(row=1, column=6)
# Units frame
units_frame.pack()
unitslabel_frame.grid(row=0, column=0, columnspan=2)
unitsframe_label.pack(fill="x", expand=1)
defaultunits_optionmenu.grid(row=1, column=0, columnspan=2)
length_label.grid(row=2, column=0)
length_optionmenu.grid(row=2, column=1)
area_label.grid(row=3, column=0)
area_optionmenu.grid(row=3, column=1)
volume_label.grid(row=4, column=0)
volume_optionmenu.grid(row=4, column=1)
velocity_label.grid(row=5, column=0)
velocity_optionmenu.grid(row=5, column=1)
pressure_label.grid(row=6, column=0)
pressure_optionmenu.grid(row=6, column=1)
temperature_label.grid(row=7, column=0)
temperature_optionmenu.grid(row=7, column=1)
force_label.grid(row=8, column=0)
force_optionmenu.grid(row=8, column=1)
energy_label.grid(row=9, column=0)
energy_optionmenu.grid(row=9, column=1)
power_label.grid(row=10, column=0)
power_optionmenu.grid(row=10, column=1)

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
