import random
def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

list = random.sample(range(1,30), 12)
print(list)
print(list_ends(list))