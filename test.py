#
# test.py
# Copyright James Robinson 2018
# All rights reserved.
#
NA = "N/A: Not Assigned, Defult Value"

class Charecter():

	def __init__(self,name = "N/A", age = "N/A", strengths = "N/A", weaknesses = "N/A", shoeSize = "N/A"):

		 self.name = name
		 self.age = age
		 self.strengths = strengths
		 self.weaknesses = weaknesses
		 self.shoeSize = shoeSize

	def PrintValues(self):
		
		print("Your Charecter's name is {name}.\nTheir age is {age}.\n\nTheir weaknesses are {weaknesses}.\nTheir strengths are {strengths}.\n\nTheir shoe size is {shoeSize}".format(name = self.name, age = self.age, strengths = self.strengths, weaknesses = self.weaknesses, shoeSize = self.shoeSize))

	def SetValues(self):

		self.name = input("Enter your name: ")
		self.age = input("Enter your age: ")
		self.strengths = input("Enter your strengths: ")
		self.weaknesses = input("Enter your weaknesses: ")
		self.shoeSize = input("Enter your shoe size: ")


char = Charecter()

char.SetValues()
char.PrintValues()
