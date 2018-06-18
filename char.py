# Copyright James Robinson 2018
# Create your charecter

# Classes
class Charecter():

	def __init__(self,name = "N/A"):




# Introduction
print("Create your charecter")


# Variables
name = input("What is your name? ")
age = input("How old is your charecter? ")
strenghts = input("What are your character's strengths? ")
weaknesses = input("What are your character's weaknesses? ")
shoeSize = input("What shoe size is your charecter? ")
 
# Outputs
print("\n--------------------\n")
print("Your character's anme is", name)
print("Your character is", age, "years old")
print("\n")
print("Strengths:", strenghts)
print("Weknesses:\n", weaknesses)

if int(shoeSize) <= 5:
    print("Your charecter has small feet!")

elif int(shoeSize) >= 8:
    print("Your charecter has BIG feet!\n")
    

# Ending
print(name, "says, Thanks for creating me!")
    
