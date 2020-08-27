import random

def list_to_set(list):
    retSet = set()
    for element in list:
        retSet.add(element)

    return retSet

list = [1,2,3,4,5,5,5]
print(list)
print(list_to_set(list))