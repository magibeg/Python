#Just random list manipulation

cars = ["Ford", "Honda", "Toyota", "GM", "Lexus", "BMW"]
print(cars)
print("-------------")

#Delete first entry
del cars[0]
print(cars)
print("-------------")

#add an entry to the end
cars.append("Mazda")

#print in alphabetical order
cars.sort()
print(cars)
print("-------------")
#reverse alphabetical order
#can also do cars.reverse()
cars.sort(reverse = True)
print(cars)

print("-------------")
#another way to print the list
print(cars[0:])

print("-------------")
print(cars[-2:])

print("-------------")
#print the list using a for loop
for i in cars:
    print(i)

print("-------------")
#print the list using a specific range
for i in cars[1:3]:
    print(i)