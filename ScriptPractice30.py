import random

lines = []
with open("SOWPODS.txt", 'r') as f:
    for l in f:
        lines.append(l.rstrip())

randomWord = lines[random.randrange(0, len(lines)-1)]
print(randomWord)
