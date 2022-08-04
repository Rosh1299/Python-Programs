# Write a Python program to get a single string from two given
# strings, separated by a space and swap the first two characters
# of each string. Go to the editor
# Sample String: 'abc', 'xyz'
# Expected Result: 'xyc abz'


from unittest import result


def swap_string(str1, str2):
    newstr1 = str2[:2]+str1[-1]
    newstr2 = str1[:2]+str2[-1]
    return f"{newstr1} {newstr2}"


print(swap_string('abc', 'xyz'))


# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def add_ing(word):
    if word.endswith('ing'):
        return word+"ly"
    else:
        return word+"ing"


print(add_ing('ping'))


# Write a Python function that takes a list of words and return the
# longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def find_largest_word(*words):
    wordlist = []
    for word in words:
        wordlist.append((len(word), word))
    wordlist.sort()
    return wordlist[-1][0], wordlist[-1][1]


result = find_largest_word('India', 'London', 'Australia')
print("Longest word:-", result[1])
print("Length of longest word:-", result[0])


# Write a Python program to change a given string to a new string
# where the first and last chars have been exchanged.

def exchange_char(str):
    return str[-1]+str[1:-1]+str[0]


print(exchange_char('abcd'))
