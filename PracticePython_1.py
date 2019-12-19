#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they 
#will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and 
#printing out that many copies of the previous message. (Hint: order of 
#operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import date

age = int(input("What is your age?"))
name = input("What is your name?")
print_count = int(input("Print output count?"))

year_to_add = 100-age

current_year = date.today().year

output_year = current_year + year_to_add

for index in range(print_count):
	print("Hi "+name +" you will be 100 in "+ str(output_year)+"\n")