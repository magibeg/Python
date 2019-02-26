#testing out some error handling

firstNumber = float(input("Please enter the first number: "))
secondNumber = float(input("Please enter the second number: "))

try:
    total = firstNumber / secondNumber
except:
    print("Something went wrong")

print(total)