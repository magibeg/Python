#From Chapter 1 in Automate the Boring Stuff
#This program will ask for a name and say hello

#Ask for a name and grab input
print("What is your name?")
myName = input()

#Print their name back to them
print("Hello " + myName + "! It is good to meet you!")

#Tell them the length of their name
print("The length of your name is: ")
print(len(myName))

#Ask for their age
print("What is your age?")
myAge = input()

#Print how old they will be in a year
print("You will be " + str(int(myAge) + 1) + " in a year!")