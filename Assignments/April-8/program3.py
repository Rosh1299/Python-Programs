from array import array
# Using List
# array1 = []
# print("Enter values for Array")
# for i in range(0, 8):
#     elements = int(input("Enter Value: "))
#     array1.append(elements)
# print("Array:", array1)

# element = int(input("Enter element to find its occurence in array:-"))
# if element in array1:
#     count = array1.count(element)
#     print(f"Entered element {element} occurs {count} times .")
# else:
#     print("Element not present in array.")

# Using Array
array1 = array("i")
print("Enter values for Array")
for i in range(0, 8):
    elements = int(input("Enter Value: "))
    array1.append(elements)
print("Array:", array1)

element = int(input("Enter element to find:-"))
if element in array1:
    index_of_element = array1.index(element)
    print(f"Entered element found at index number {index_of_element}.")
else:
    print("Element not present in array.")
