a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
check = int(input("Enter a number to check by: "))
x = []

for i in a:
    if i <= check:
        x.append(i)

print(x)