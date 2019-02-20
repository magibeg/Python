#Does various calculations

area = 0
height = 10
width = 20

#calculate the area of a triangle
area = width * height * 2
print("The triange is " + str(height) + " tall and " + str(width) + " wide.")
#print formatted float value with 2 decimal places
print("The area of the triangle is %.2f" % area)
print("The area of the triangle is {0:f}".format(area))
#printing the formatted deciaml number with right justied to take up 6 spaces with leading 0's
print("My favorite number is %06d !" % 42)


print("I have {0:d} cats".format(6))