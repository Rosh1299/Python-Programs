# def dec_to_binary(num):
#     binary_num = ''
#     print("Decimal Number:", num)
#     if num <= 1024:
#         while num > 0:
#             rem = num % 2
#             binary_num = str(rem)+binary_num
#             num = num//2
#     else:
#         pass
#     print("Binary Number:", binary_num)


# num = int(input("Enter a number(0 to 1024):"))
# dec_to_binary(num)


# program to count vowel in string

# count = 0
# string1 = input("Enter a word or sentence:")

# for vowel in string1:
#     if vowel in 'aeiouAEIOU':
#         count += 1
# print("Number of Vowels in entered string:", count)


string1 = input("Enter a word or sentence:")
int_list = []
for i in string1:
    if i in "0123456789":
        int_list.append(i)
print(int_list)
