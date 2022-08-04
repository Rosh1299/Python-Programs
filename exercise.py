# write the program to find most repeated character in string.


sentence = "This is a common interview quEstion"
# sentence = "Define clear measure if success and a plan to achieve them."
char_dict = {}
for char in sentence:
    if char != " ":
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

char_dict_sorted = sorted(
    char_dict.items(),
    key=lambda val: val[1],
    reverse=True)
print(char_dict_sorted)
print(char_dict_sorted[0])
