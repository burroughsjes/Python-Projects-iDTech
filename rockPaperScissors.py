import random

playAgain = "yes"
score = 0 #score for player/user
cscore = 0 #score for computer

print("Welcome to the rock, paper, scissors game! You will be playing against the computer.")

while (playAgain == "yes"):
    computerNum = random.randint(0,2)

    #this is a list that will assign each random number to one of these, starts with 0 then 1 then 2
    rps = ["rock", "paper", "scissors"]

    computerMove = rps[computerNum]

    userMove = input("\nWill you play rock, paper, or scissors?\n").lower()
    
    # conditions for when computer whens
    if ((userMove == "rock" and computerMove == "paper") or
        (userMove == "paper" and computerMove == "scissors") or
        (userMove == "scissors" and computerMove == "rock")):
        print("The computer played " + computerMove + ". The computer wins!")
        cscore += 1
    elif userMove == computerMove:
        print("The computer played " + computerMove + ". You tied.")
    # conditions for when player whens
    else:
        print("The computer played " + computerMove + ". You win!")
        score += 1

    print("\nComputer: " + str(cscore) + "\nYou: " + str(score))
    playAgain = input("\nDo you want to play again?\n").lower()

print("\nFinal scores: " + "\nComputer: " + str(cscore) + "\nYou: " + str(score))
