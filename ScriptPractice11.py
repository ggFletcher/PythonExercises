def checkPrime(num):
    list = []
    for i in range(1,num):
        if num % i == 0:
            list.append(i)
    if list == [1]:
        return True
    else:
        return False

num = int(input("Enter a number to check for prime-ness: "))
if checkPrime(num):
    print(num, "is prime!")
else:
    print(num, "is not prime!")