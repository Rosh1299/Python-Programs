# Accept Values from user; store it in array;
# then print the second lowest number from that array"

value = []
for i in range(5):
    num = int(input("Enter value:"))
    value.append(num)
# print(len(value))
print("Entered numbers are:", value)
# for sorting
for i in range(len(value)):
    for j in range(len(value)-1):
        if value[j] > value[j+1]:
            value[j], value[j+1] = value[j+1], value[j]

print("Sorted List:", value)
print("Second lowest number in list is :", value[1])
