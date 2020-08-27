# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, 
# will have in your head a number between 0 and 100. The program will guess a number, 
# and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.)
# until you hit the number. But that’s not an optimal guessing strategy. 
# An alternate strategy might be to guess 50 (right in the middle of the range), 
# and then increase / decrease by 1 as needed. After you’ve written the program, 
# try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

import random

def guessingGame(min, max):
    guess = False
    tries = 1

    num = int((min + max) / 2)
    newMin = min
    newMax = max

    while guess == False:
        print("I guess - ", num)
        feedback = input("Is your number higher(H/h), lower(L/l), or was I right on(R/r)? ")

        if feedback.lower() == 'h':
            newMin = num
            tries += 1
        elif feedback.lower() == 'l':
            newMax = num
            tries += 1
        elif feedback.lower() == 'r':
            print("It only took me ", tries, " tries!")
            guess = True
        elif feedback.lower() == 'q':
            print("You only let me have ", tries, " tries!")
            guess = True

        num = int((newMax + newMin) / 2)

guessingGame(0,100)
