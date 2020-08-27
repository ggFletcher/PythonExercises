name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
repeat = int(input("How many times would you like to output the message?: "))

for x in range(repeat):
    print("\n")
    print(name, "- You will be 100 years old in", 100 - age + 2020)
