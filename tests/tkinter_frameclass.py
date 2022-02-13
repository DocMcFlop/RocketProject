from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Window Example')
root.iconbitmap('icon.ico')
root.geometry("400x400")

#class Item:
#
#	def __init__(self, name: str, price: float, quantity=0):
#		# Run validations to the received arguments
#		assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#		assert quantity >= 0, f"price {quantity} is not greater than or equal to zero!"
#
#		# Assign to self object
#		self.name = name
#		self.price = price
#		self.quantity = quantity
#
#	def calculate_total_price(self):
#		return self.price * self.quantity

#item1 = Item("Phone", 100, -5)

#item2 = Item("Laptop", 1000, 10)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

# Label:
#	[1]: Text
# Entry:
#   [1]: variable_name
#   [2]: unit
# OptionMenu:
#   [1]: Options list
# CheckButton:

force_frame = [[root,"Label"],
			   ["Thrust: ", "Entry", "[N]"],
			   ["Atmospheric Pressure: ", "Entry", "[Pa]"]
			   ]

test_frame = [[root,"Label"],
			   [["Label","Thrust: "], ["Entry","thrust","force"], ["Label","[N]"]],
			   [["Label","Atmopsheric Pressure: "], ["Entry","atmospheric_pressure","pressure"], ["Label","[N/m^2]"]],
			   [["Label","Chamber Volume: "], ["Entry","chamber_volume","volume"], ["Label","[m^3]"]],
			   ]

#print(test_frame[1][0][1])

entries = []

class FrameConstructor:

	# Initialization
	def __init__(self, data_list):

		self.frame = data_list[0][0]
		self.label = data_list[0][1]
		self.data_list = data_list

	# Function to construct frame
	def construct_frame(self):

		# Iterate through data list containing frame parameters
		for item_pos, item in enumerate(self.data_list):

			# Check for the first item in the list
			if item_pos == 0:
				Label(self.frame, text=self.label).grid(row=0, columnspan=len(self.data_list[1]))
				continue

			# Iterate through the lists in the list
			for subitem_pos, sub_item in enumerate(item):
				if sub_item[0] == "Entry":
					entry = Entry(self.frame)
					entry.grid(row=item_pos, column=subitem_pos)
					entries.append([sub_item[1], entry, sub_item[2]])

				elif sub_item[0] == "Label":
					Label(self.frame, text=sub_item[1]).grid(row=item_pos, column=subitem_pos)
				elif sub_item[0] == "OptionMenu":
					pass
				elif sub_item[0] == "Checkbutton":
					pass
					

frame1 = FrameConstructor(test_frame).construct_frame()

# Entries variable
# [entry value, variable name for searching, variable type]

for item in entries:
	print(item[0])
	print(item[2])

root.mainloop()
#propellant1.density = 1350
#propellant1.viscosity = 0.004
#propellant1.prandtl_number = 450
#propellant1.conductivity = 300

#root.mainloop()