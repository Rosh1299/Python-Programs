# Write a Python program to count the number of
# characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


def frequency(word):
    dict1 = {}
    for i in word:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


print(frequency("Google"))
