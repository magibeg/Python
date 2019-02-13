#No complete program this chapter so applying a loop and condition

keepRunning = True

yourName = input("What is your name? ")

while keepRunning == True:
    print("Welcome " + yourName)
    keepPlaying = input("Do you want to play a game? (yes/no): ")
    if keepPlaying == "yes":
        print("This game doesn't do anything")
    else:
        print("You're leaving the game :(")
        keepRunning = False
    print("This is the end of the loop")