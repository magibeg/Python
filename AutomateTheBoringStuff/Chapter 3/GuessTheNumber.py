#This is a guess the number game

import random

#function to randomize the number
def randomNumber(genSecretNumber):
    genSecretNumber = random.randint(lowNum,highNum)
    return genSecretNumber

#creates and sets some of the basic variables needed to run
highNum = 20
lowNum = 1
guessesAllowed = 6
guessesTaken = 0
secretNumber = 0

#Assigns a random number to secret number by calling the function
secretNumber = randomNumber(secretNumber)

#Lets the user know what the low and high numbers are
print("I am thinking of a number between " + str(lowNum) + " and " + str(highNum))

#Main game loop that runs until the user guesses the number or runs out of guesses
while guessesTaken < guessesAllowed:
    #counts up the number of guesses taken
    guessesTaken = guessesTaken + 1

    #takes the guessed number and makes it an int
    guess = int(input("What is your guess: "))

    #checks to see if the user was lower, higher, or exact in their guess
    if guess <  secretNumber:
        print("Your number is too low. " + "You have " + str(guessesAllowed - guessesTaken) + " guesses left.")
    elif guess > secretNumber:
        print("Your guess is too high. " + "You have " + str(guessesAllowed - guessesTaken) + " guesses left.")
    elif guess == secretNumber:
        print("You guessed the number!")
        #tell the user how many guesses it took
        print("It took you " + str(guessesTaken) + " guesses to get it correct!")
        #give them the option to play again, reset the number of guesses, and get a new random number
        playAgain = input("Would you like to play again? (yes/no): ")
        if playAgain == "yes":
            guessesTaken = 0
            secretNumber = randomNumber(secretNumber)
        else:
            break
