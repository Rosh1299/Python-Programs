
number = int(input("Enter Number:"))

sum_of_digit = 0

while number > 0:
    digit = number % 10
    sum_of_digit = sum_of_digit+digit
    number = number//10
print("Sum of digit:", sum_of_digit)
