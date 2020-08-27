import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = int(input("How long do you want your password to be? "))
password =  "".join(random.sample(s,passlen))

print(password)