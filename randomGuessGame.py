import random

count = 0 # keeps track of number of tries to guess number
playAgain = "yes"

print("Welcome to the guessing game!")

while (playAgain == "yes"): 

    num = random.randint(0, 100)
    guess = int(input("\nGuess a number between 0 and 100\n"))

    while guess != num:
        count += 1
        
        if (guess > 100 or guess < 0):
            print("Not a valid input")
        elif (guess > num):
            if ((guess - num) <= 5): print("Your guess is just a tad bit high")
            else: print("Your guess is too high")
        elif (guess < num):
            if ((num - guess) <= 5): print("Your guess is just a tad bit low")
            else: print("Your guess is too low")

        guess = int(input("\nGuess a number between 0 and 100\n"))

    print("\nYou guessed correctly! The number was " + str(num) + "\nIt took you " + str(count) + " tries.")

    repeat = input("Do you want to play again?\n").lower()