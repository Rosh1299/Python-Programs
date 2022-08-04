# arrays
# it stores data having same datatype.

from array import array


a = array("i", [1, 2, 3])
a[0] = 11
a.append(4)
print(a)
a.append

# from array import array

# arr1 = array("i")
# a = int(input("Enter 1st elements for array1-:"))
# arr1.append(a)
# b = int(input("Enter 2nd elements for array1-:"))
# arr1.append(b)
# c = int(input("Enter 3rd elements for array1-:"))
# arr1.append(c)

# arr2 = array("i")
# a = int(input("Enter 1st elements for array1-:"))
# arr2.append(a)
# b = int(input("Enter 2nd elements for array1-:"))
# arr2.append(b)
# c = int(input("Enter 3rd elements for array1-:"))
# arr2.append(c)

# arr3 = array("i")

# for i in arr1:
#     if i in arr2:
#         arr3.append(i)
# print("Common Elements of both array:-", arr3)


# arr4 = array("i")
# for i in arr1:
#     if i not in arr2:
#         arr4.append(i)

# for j in arr2:
#     if i not in arr1:
#         arr4.append(j)

# print(arr4)

class Product:
    pass


p = Product()
for name in Product.__dict__:
    print(name)
