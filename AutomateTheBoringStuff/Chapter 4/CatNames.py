#Asks the user to type in cat names until they enter a blank input

catNames = []

while True:
    name = input("Enter the name of the cat " + str(len(catNames)+ 1) + " or enter nothing to stop: ")

    if name == "":
        break
    catNames = catNames + [name]
print("That cat names are: ")
for name in catNames:
    print("     " + name)