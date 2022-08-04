# addition of digit having odd index
num = input("Enter a number:")
sum = 0
for i in num:
    if num.index(i) % 2 == 1:
        sum += int(i)

print(sum)
