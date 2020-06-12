import random

playAgain = True
score = 0
cscore = 0

print("Welcome to the rock, paper, scissors game! You will be playing against the computer.")

while playAgain == True:
    computerNum = random.randint(0,2)

    #this is a list that will assign each random number to one of these, starts with 0 then 1 then 2
    rps = ["rock", "paper", "scissors"]

    computerMove = rps[computerNum]


    #print("The computer picked " + computerMove)

    #.lower makes the input converted to all lowercase
    userMove = input("\nWill you play rock, paper, or scissors?\n").lower()
    

    if userMove == "rock" and computerMove == "paper":
        print("The computer played " + computerMove + ". The computer wins!")
        cscore += 1
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    elif userMove == "paper" and computerMove == "scissors":
        print("The computer played " + computerMove + ". The computer wins!")
        cscore += 1
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    elif userMove == "scissors" and computerMove == "paper":
        print("The computer played " + computerMove + ". You win!")
        score += 1
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    elif userMove == "paper" and computerMove == "rock":
        print("The computer played " + computerMove + ". You win!")
        score += 1
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    elif userMove == "rock" and computerMove == "scissors":
        print("The computer played " + computerMove + ". You win!")
        score += 1
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    elif userMove == computerMove:
        print("The computer played " + computerMove + ". You tied.")
        print("\nComputer: " + str(cscore) + "\nYou: " + str(score))


    play = input("\nDo you want to play again?\n").lower()

    if play == "yes":
        playAgain = True
    elif play == "no":
        playAgain = False
        print("\nFinal scores: " + "\nComputer: " + str(cscore) + "\nYou: " + str(score))
