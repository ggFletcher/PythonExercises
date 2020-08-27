def reverse_string(string):
    split = string.split(" ")
    reverseList = [ele for ele in reversed(split)]
    return " ".join(reverseList)

string = input("Input a sentence: ")
print(reverse_string(string))