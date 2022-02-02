from tkinter import *
from PIL import ImageTk,Image
import sqlite3

#root = Tk()
#root.title('Window Example')
#root.iconbitmap('icon.ico')
#root.geometry("400x400")

class Item:

	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		assert price >= 0, f"Price {price} is not greater than or equal to zero!"
		assert quantity >= 0, f"price {quantity} is not greater than or equal to zero!"

		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):
		return self.price * self.quantity

item1 = Item("Phone", 100, -5)

item2 = Item("Laptop", 1000, 10)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#propellant1.density = 1350
#propellant1.viscosity = 0.004
#propellant1.prandtl_number = 450
#propellant1.conductivity = 300

#root.mainloop()