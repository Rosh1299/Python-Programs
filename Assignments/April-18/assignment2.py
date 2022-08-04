list1 = []
list2 = []
list3 = []
# for adding element in list1
print("Accepting Array-1")
for i in range(4):
    num = int(input("Enter number:"))
    list1.append(num)

print("Accepting Array-2")
# for adding element in list2
for i in range(4):
    num = int(input("Enter number:"))
    list2.append(num)

# for creating another list for unique numbers of both list
for i in range(len(list1)):
    if list1[i] not in list2:
        list3.append(list1[i])
for i in range(len(list2)):
    if list2[i] not in list1:
        list3.append(list2[i])

print("New Array:", list3)
