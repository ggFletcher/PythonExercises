import random
list1 = random.sample(range(100), k=10)
list2 = random.sample(range(100), k=10)
similar = []
print(list1)
print(list2)

for i in list1:
    if i in list2:
        if i in similar:
            continue
        else:
            similar.append(i)

print(similar)