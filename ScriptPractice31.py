#! /usr/bin/python3
import random

if __name__ == '__main__':
    print("Welcome to hangman!!")
    lines = []
    with open("SOWPODS.txt", 'r') as f:
        for l in f:
            lines.append(l.rstrip())

    word = lines[random.randrange(0, len(lines)-1)]

    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("guess letter: ")
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            print(''.join(guessed))
            if letter != '':
                lstGuessed.append(letter.upper())
                letter = input("guess letter: ")

        if '_' not in guessed:
            print("You won!!")
            break