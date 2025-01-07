#A program to calculate the age of a user
from datetime import datetime
#Get current year
current_year = datetime.now().year
#Take user input
name = (input("What is your name?\n"))
age = int(input("How old are you?\n"))
#Calculate the year of birth
year_of_birth = current_year - age
print (f"Hello, {name}! You were born in {year_of_birth}.")