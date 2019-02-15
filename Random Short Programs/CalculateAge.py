#This program gives you interesting stats about your age

print("Let's learn some fun facts about your age.")

age = int(input("How old are you?"))
days = age * 365
hours = days * 12
minutes = hours * 60
seconds = minutes * 60

print("You are " + str(days) + " days old.")
print("You are " + str(hours) + " days old.")
print("You are " + str(minutes) + " days old.")
print("You are " + str(seconds) + " days old.")
print("Wow you're old!")