

unit_num = {1: "One ", 2: "Two ", 3: "Three ",
            4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine ",
            10: "Ten ", 11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ",
            15: "Fifteen ", 16: "Sixteen ", 17: "Seventeen ", 18: "Eighteen ", 19: "Nineteen "}
tens_num = {20: "Twenty ", 30: "Thiry ",
            40: "Fourty ", 50: "Fifty ", 60: "Sixty ", 70: "Seventy ", 80: "Eighty ", 90: "Ninety "}


def numbertoword(n, suffix):
    if n == 0:
        return ''
    elif n <= 19:
        return unit_num[n]+suffix
    elif n in tens_num:
        return tens_num[n]+suffix
    else:
        return tens_num[n-n % 10]+unit_num[n % 10].lower()+suffix


def convert(num):
    result = numbertoword((num//100000) % 1000, "Lakh ")
    result += numbertoword((num//1000) % 100, "Thousand ")
    result += numbertoword((num//100) % 10, "Hundred ")
    result += numbertoword((num % 100), "")
    return result


num = int(input("Enter a number:"))
if num == 0:
    print("Zero")
else:
    print(convert(num))
