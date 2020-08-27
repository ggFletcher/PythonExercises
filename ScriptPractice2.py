num = int(input("Please enter a number: "))
check = int(input("Please enter a number to check by: "))

if(num % check == 0):
    print(num, "is divisible by", check)
else:
    print(num, "is not divisible by", check)

if(num % 4 == 0):
    print(num, "is a multiple of 4!")

if(num % 2 == 0):
    print(num, "is even!")
elif(num % 2 != 0):
    print(num, "is odd!")