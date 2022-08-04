# unit_num = {1: "One ", 2: "Two ", 3: "Three ",
#             4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine ", 10: "Ten ",
#             11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ", 15: "Fifteen ", 16: "Sixteen ", 17: "Seventeen ",
#             18: "Eighteen ", 19: "Ninteen ", }

# tens_num = {20: "Twenty ", 30: "Thiry ",
#             40: "Fourty ", 50: "Fifty ", 60: "Sixty ", 70: "Seventy ", 80: "Eighty ", 90: "Ninety "}

# hundread_num = {100: "One Hundread ", 200: "Two Hundread ", 300: "Three Hundread ",
#                 400: "Four Hundread ", 500: "Five Hundread ", 600: "Six Hundread ",
#                 700: "Seven Hundread ", 800: "Eight Hundread ", 900: "Nine Hundread "}

# num = int(input("Enter a Number:"))

# num_length = len(str(num))
# if num_length == 1 or num <= 19:
#     print(unit_num[num])
# elif num_length == 2 and num > 19:
#     digi_list = []
#     while num > 0:
#         digit = num % 10
#         digi_list.append(digit)
#         num = num // 10
# print(digi_list)


class Number:
    def __init__(self, val):
        self.__val = val

    def show(self):
        print(self.__val)


a = Number(7)
