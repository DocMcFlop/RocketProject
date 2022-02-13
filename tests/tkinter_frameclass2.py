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

entries = []

frame = ttk.Frame(root)
frame.pack()

# Label:
#	[1]: Text
# Entry:
#   [1]: variable_name
#   [2]: unit
# OptionMenu:
#   [1]: Options list
# CheckButton:



test_frame = [[["Label","Thrust: "], ["Entry","thrust","force","[N]"]],
			  [["Label","Atmopsheric Pressure: "], ["Entry","atmospheric_pressure","pressure","[N/m^2]"]],
			  [["Label","Chamber Volume: "], ["Entry","chamber_volume","volume","[m^3]"]],
			  [["Label","Fuel: "], ["OptionMenu","fuel", "string","[~]", ["Jet-A","Methane","Doo-doo"]]],
			  [["Label","Oxidizer: "], ["OptionMenu","oxidizer", "string","[~]", ["LOX","Nitrous Oxide","Fluorine"]]]
			  ]

test_frame2 = [
			   [["Label","Vacuum Thrust: "], ["Entry","vacuumthrust","force","[N]"]],
			   [["Label","Vacuum Pressure: "], ["Entry","vacuum_pressure","pressure","[N/m^2]"]],
			   [["Label","Chamber Volume: "], ["Entry","nozzle_volume","volume","[m^3]"]],
			   [["Label","Fuel: "], ["OptionMenu","cryogenicfuel", "string","[~]", ["Jet-A","Methane","Doo-doo"]]],
			   [["Label","Oxidizer: "], ["OptionMenu","cryogenicoxidizer", "string","[~]", ["LOX","Nitrous Oxide","Fluorine"]]]
			   ]

class FrameConstructor:

	# Initialization
	def __init__(self, frame, frame_title, frame_row, frame_column, data_list):

		self.frame = frame
		self.frame_title = frame_title
		self.row = frame_row
		self.column = frame_column
		self.data_list = data_list
		self.class_frame = ttk.Frame(self.frame, borderwidth=5, relief="groove")

	# Function to construct frame
	def construct_frame(self):

		#self.labelframe = ttk.Frame(self.class_frame, borderwidth=5, relief="groove")
		#ttk.Label(self.class_frame, text=self.frame_title, borderwidth=5, relief="groove").grid(row=0, column=1)
		#self.labelframe.grid(row=0, column=1, columnspan=3)

		#ttk.Label(self.class_frame, relief="groove").grid(row=0, column=0)

		# Iterate through data list containing frame parameters
		for item_pos, item in enumerate(self.data_list):

			# Modify item position for grid definition since the label occupise row=0 
			self.item_row = item_pos+1

			# Iterate through the lists in the list
			for subitem_pos, sub_item in enumerate(item):

				self.item_column = subitem_pos

				# Display option label
				if sub_item[0] == "Label":
					ttk.Label(self.class_frame, text=sub_item[1]).grid(row=self.item_row, column=self.item_column)

				# Check to see if the item is an entry widget
				elif sub_item[0] == "Entry":
					entry = ttk.Entry(self.class_frame, width=8)
					entry.grid(row=self.item_row, column=self.item_column)
					label = ttk.Label(self.class_frame, text=sub_item[3])
					label.grid(row=self.item_row, column=self.item_column+1)
					# Append the entries variable
					entries.append([sub_item[1], entry, label, sub_item[2]])

				# Check to see if the item is an optionmenu widget
				elif sub_item[0] == "OptionMenu":
					var = StringVar()
					option = ttk.OptionMenu(self.class_frame, var, None, *sub_item[-1])
					option.grid(row=self.item_row, column=self.item_column, columnspan=2, sticky="ew")
					# Append the entries variable
					entries.append([sub_item[1],var,"~",sub_item[2]])

		ttk.Label(self.class_frame, text=self.frame_title, borderwidth=5, relief="groove", anchor="center").grid(row=0, columnspan=3, sticky="ew")
		# Pack the frame using the grid format
		self.class_frame.grid(row=self.row, column=self.column)

frame1 = FrameConstructor(frame=frame, data_list=test_frame, frame_title="Label1", frame_row=0, frame_column=0).construct_frame()
frame2 = FrameConstructor(frame=frame, data_list=test_frame2, frame_title="Label2", frame_row=0, frame_column=1).construct_frame()


def update():
	for item in entries:
		print(item[1].get())

mybutton = ttk.Button(frame, text="Update", command=update)
mybutton.grid()

root.mainloop()
