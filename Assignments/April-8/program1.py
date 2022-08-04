arr1 = []
print("Enter values for Array-1")
for i in range(3):
    elements = int(input("Enter the values: "))
    arr1.append(elements)
print("Values for Array-2")
arr2 = []
for i in range(3):
    input1 = int(input("Enter the values: "))
    arr2.append(input1)

arr3 = []
arr4 = []

for i in arr1:
    if i in arr2:
        arr3.append(i)
print("Common values from array1 and array2.\n", arr3)

for i in arr1:
    if i not in arr2:
        arr4.append(i)
for j in arr2:
    if j not in arr1:
        arr4.append(j)
print("Uncommon Values from array1 and array2.\n", arr4)
