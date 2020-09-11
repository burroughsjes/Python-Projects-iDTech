import random

playAgain = "yes"

while (playAgain == "yes"):
    # choices the magic 8 ball could choose
    opt = ["It is certain.", "Don't count on it.", "As I see it, yes.", "Reply hazy, try again.", "My reply is no.", "Without a doubt.", "Ask again later.", "Yes-definitely.", "Concentrate and ask again.", "My sources say no."]
                
    ansNum = random.randint(0, len(opt) - 1)

    ans = opt[ansNum]

    print("Welcome to the Magic 8 Ball!")
    questions = input("Input your yes or no question below:\n\n")
    print("\n" + ans)

    again = input("\nDo you want to play again?\n").lower()
