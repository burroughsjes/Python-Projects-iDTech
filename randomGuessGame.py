import random

count = 0
playAgain = True

print("Welcome to the guessing game!")

while playAgain == True: 

    num = random.randint(0, 100)
    guess = int(input("\nGuess a number between 0 and 100\n"))

    while guess != num:
        count += 1
        if guess > num and guess <= 100 and (guess - num) > 5:
            print("Your guess is too high")
        elif guess > num and guess <= 100 and (guess - num) <= 5:
            print("Your guess is just a tad bit high")
        elif guess < num and guess >= 0 and(num - guess) > 5:
            print("Your guess is too low")
        elif guess < num and guess >= 0 and (num - guess) <= 5:
            print("Your guess is just a tad bit low")
        else:
            print("Not a valid input")

        guess = int(input("Guess a number between 0 and 100\n"))

    print("You guessed correctly! The number was " + str(num) + "\nIt took you " + str(count) + " tries.")

    repeat = input("Do you want to play again?\n").lower()

    if repeat == "yes":
        playAgain = True
    elif repeat == "no":
        playAgain = False
