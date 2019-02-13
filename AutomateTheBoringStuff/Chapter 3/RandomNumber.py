#Magic 8 ball style random number generator with the addition of a loop

import random

#The function getAnswer returns a phrase based on the random number generated
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again later"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

keepPlaying = True

print("Welcome to the fortune teller program!")
print("Simply imagine the question and i'll give you the answer")

while keepPlaying == True:
    #Grabs a random number between 1 and 9 and assigns it to the variable r
    r = random.randint(1,9)
    #The variable fortune equals the returned value of r
    fortune = getAnswer(r)
    #Displays the message to the user
    print(fortune)

    playAgain = input("Would you like to keep playing? (yes/no)")
    if playAgain == "yes":
        print("Again it is!")
    else:
        print("No more fortunes will be given today")
        keepPlaying = False
