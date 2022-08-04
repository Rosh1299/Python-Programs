num = int(input("Enter number between 1-9:"))

numlist = []

if num >= 5:
    for i in range(10-num, num+1):
        numlist.append(i)
    reverse_numlist = numlist[::-1]
else:
    for i in range(10-num, num-1, -1):
        numlist.append(i)
    reverse_numlist = numlist[::-1]

print(numlist)
print(reverse_numlist)

total = 0
for i in range(len(numlist)):
    if numlist[i] == reverse_numlist[i]:
        print(numlist[i], "=", reverse_numlist[i])
        total = numlist[i]+total
        break
    else:
        result = numlist[i]+reverse_numlist[i]
        print(numlist[i], "+", reverse_numlist[i],
              "=", result)
    total = result + total
print("Total=", total)
