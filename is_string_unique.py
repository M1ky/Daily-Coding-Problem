'''
Implement an algorithm to determine if a string has all
unique characters.
'''

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"


def normalize_str(input_str):
    # function that removes spaces from string and converts all characters to lower
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def is_unique_1(input_str):
    # loop through string and if the character is not in dictionary than add it to the dictionary
    # this uses a new data structure which will use O(n) space
    d = dict()
    for char in input_str:
        if char in d:
            return False
        else:
            d[char] = 1
    return True


def is_unique_2(input_str):
    # set function returns all unique characters
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    # this assumes that string will contain only letters
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in input_str:
        if char in alpha:
            alpha = alpha.replace(char, "")
        else:
            return False
    return True


unique_str = normalize_str(unique_str)
non_unique_str = normalize_str(non_unique_str) 

print(unique_str)
print(non_unique_str)

print(is_unique_1(unique_str))
print(is_unique_1(unique_str))

print(is_unique_2(non_unique_str))
print(is_unique_2(non_unique_str))

print(is_unique_3(unique_str))
print(is_unique_3(non_unique_str))