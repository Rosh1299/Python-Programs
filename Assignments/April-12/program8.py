# Assignment 8  write a program to print the frequency of each character in a string.
# 	    if input is :- “Hello friend”
# 	    Output should be
#     		d: 1
#     		e: 2
#     		f: 1
#  	(continued for all character in the string)"

char_count = {}
str1 = input("Enter any sentence:-")
for char in str1.lower():
    if char != " ":
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

for i in char_count:
    print(i, ":", char_count[i])
