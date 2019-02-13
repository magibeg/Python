#Another magic 8 ball style of program, this time with a list

import random

messages = ["It is certain", 
    "It is decidedly so", 
    "Yes, definitely",
    "Reply hazy, try again later",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful"]

playAgain = "yes"

print("Welcome to the new Magic 8 ball program!")
while playAgain == "yes":
    print(messages[random.randint(0, len(messages) -1)])
    playAgain = input("Would you like to try again? (yes/no)")
    if playAgain != "yes":
        print("Thank you for listening, goodbye")