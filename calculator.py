def calculator(num1, num2, action):
    if action == "+":
        print(f"{num1}{action}{num2}=", num1+num2)
    elif action == '-':
        print(f"{num1}{action}{num2}=", num1-num2)
    elif action == '*':
        print(f"{num1}{action}{num2}=", num1*num2)
    elif action == '/':
        print(f"{num1}{action}{num2}=", num1/num2)


while True:
    str1 = input("Enter Expression:")
    num1 = int(str1[0])
    action = str1[1]
    num2 = int(str1[2])
    calculator(num1, num2, action)


# eval is function to calculate expression given in the string
# print(eval("45+10-30*2"))
