# this is a comment
# this is a print method. Print will echo out anything inside the 
# () round backets to the terminal when we run the file
print("This is my very first python script!!")

name = "Burak"
haircolor = "Brown"
age = 39

#variables are placeholders, with dynamic values ->things that can change
#they get stored in memory and referenced later
# car1 = "Volvo"
# car2 = "Toyota"
# car3 = "Fiesta"
# this is not good


#this is an array. They let store many variables in one variable
#variable -> to help us group data
#This makes our scripting files easier to understand and work it.
cars = ["Volvo", "Toyota", "Fiesta"]

print("My name is " + name)


#input is another python 'thing' - it waits with a flashing cursor
#until you type something and hit enter
alternateName = input("What is YOUR name?")

print("My name is now " + alternateName)

print("My age is " + str(age))

