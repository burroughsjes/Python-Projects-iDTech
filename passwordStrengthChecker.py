import re

# returns true if entire string is numbers
def hasAllNumbers(inputString):
    return all(char.isdigit() for char in inputString) 

def tableAdditions():
    table = [["Length", length, "+ " + str(lengthBonus)],
             ["Uppercase Letters", uppercase, "+ " + str(uppercaseBonus)],
             ["Lowercase Letters", lowercase, "+ " + str(lowercaseBonus)],
             ["Numbers", number, "+ " + str(numberBonus)],
             ["Symbols", symbol, "+ " + str(symbolBonus)],]
    return table

def tableDeductions():
    table2 = [["Letters Only", lettersOnly, "- " + str(lettersOnlyPoints)],
             ["Numbers Only", numbersOnly, "- " + str(numbersOnlyPoints)],
             ["Repeat Characters", repeat, "- " + str(repeatPoints)],
             ["Sequential Letters", sLetters, "- " + str(sLettersPoints)],
             ["Sequential Numbers", sNumbers, "- " + str(sNumbersPoints)],]
    return table2

number = 0
uppercase = 0
lowercase = 0
symbol = 0
lettersOnly = 0
lettersOnlyPoints = 0
numbersOnly = 0
numbersOnlyPoints = 0
repeat = 0
repeatPoints = 0
sLetters = 0
sLettersPoints = 0
sNumbers = 0
sNumbersPoints = 0
uppercaseBonus = 0
numberBonus = 0
lengthBonus = 0
lowercaseBonus = 0
symbolBonus = 0
count = 0
playAgain = "yes"

print("Welcome to the Password Strength Checker!\n\n")

while (playAgain == "yes"): 

    password = input("Enter your password: ")
    length = len(password)
    lengthBonus = length * 4

    # gives points if entire String is letters
    if (password.isalpha()):
        lettersOnly = length
        lettersOnlyPoints = length
        
    # gives points if entire String is numbers
    if (hasAllNumbers(password)):
        numbersOnly = length
        numbersOnlyPoints = length

    # counts number of characters that repeats often
    frequencies = {}
    for i in password:
        if (i in frequencies):
            frequencies[i] += 1
        else:
            frequencies[i] = 0
    repeat = len([freq for freq in frequencies.values() if freq > 3])
    repeatPoints = 5 * repeat

    # assigns points based on if the letters and numbers are in consecutive order or not
    for x in range(1, length):
        # dealing with letters
        if (password[x].lower() >= chr(97) and password[x].lower() <= chr(122)):
            if (ord(password[x].lower()) == ord(password[x - 1].lower()) + 1):
                sLetters += 1
        # dealing with numbers
        if (password[x].lower() >= chr(48) and password[x].lower() <= chr(57)):
            if (ord(password[x]) == ord(password[x - 1]) + 1): 
                sNumbers += 1

    sLettersPoints = sLetters * 3
    sNumbersPoints = sNumbers * 3       
        
    # adding bonuses to the score
    for x in password:
        if (x.isdigit()):
            number += 1
            numberBonus = number * 4
        if (x >= chr(65) and x <= chr(90)):
            uppercase += 1
            uppercaseBonus = (len(password) - uppercase) * 2
        if (x >= chr(97) and x <= chr(122)):
            lowercase += 1
            lowercaseBonus = (len(password) - lowercase) * 2
        if (x >= chr(33) and x <= chr(47) or x >= chr(58) and x <= chr(64) or x >= chr(91) and x <= chr(96) or x >= chr(123) and x <= chr(126)):
            symbol += 1
            symbolBonus = symbol * 6
        
    print("\n\n: Additions            :  Count  :  Points  :")
    print("————————————————————————————————————————————")

    for item in tableAdditions():
        print(":", item[0], " "*(19 - len(item[0])), ":", item[1], " "*(6-len(str(item[1]))), ":", item[2], " "*(7-len(item[2])), ":")

    print("\n\n: Deductions           :  Count  :  Points  :")
    print("————————————————————————————————————————————")

    for item in tableDeductions():
        print(":", item[0], " "*(19 - len(item[0])), ":", item[1], " "*(6-len(str(item[1]))), ":", item[2], " "*(7-len(item[2])), ":")

    # calculating final score
    score = lengthBonus + uppercaseBonus + lowercaseBonus + numberBonus + symbolBonus - lettersOnlyPoints - numbersOnlyPoints - sLettersPoints - sNumbersPoints - repeatPoints
    print("\n\nScore:", str(score))

    if score <= 20:
        print("Strength: Extremely Poorly Weak")
    elif score <= 35:
        print("Strength: Very Weak")
    elif score <= 50:
        print("Strength: Weak")
    elif score <= 80:
        print("Strength: Good")
    elif score <= 100:
        print("Strength: Strong")
    elif score <= 120:
        print("Strength: Very Strong")
    elif score > 120:
        print("Strength: Extremely Unbreakably Strong")

    again = input("\n\nDo you want to try another password?\n\n\n").lower()


