num = int(input("Enter a number to check for divisors: "))
list = []
for i in range(1,num):
    if num % i == 0:
        list.append(i)

print(list)