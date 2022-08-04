# class Bird:
#     no_of_wings = 2

#     def __init__(self, name, color):
#         self.name = name
#         self.color = color


# a = Bird('Parrot', 'Green')
# b = Bird('Crow', 'Black')

# print("Name:", a.name)
# print("Color:", a.color)
# print("Number of Wings:", a.no_of_wings)


# class Bird:
#     # class attribute
#     no_of_wings = 2

#     def __init__(self, name, color):
#         # instance attribute
#         self.name = name
#         self.color = color

#     def __del__(self):
#         print("Object Destroy")


# a = Bird('Parrot', 'Green')
# b = Bird('Crow', 'Black')

# print("Name:", a.name)
# print("Color:", b.color)


# class Number:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     # operator overriding
#     def __add__(self, other):
#         return self.a+other.a


# v1 = Number(1, 2)
# v2 = Number(3, 4)

# print(v1+v2)


# class Demo:
#     def __init__(self, a, b):
#         self.a = a
#         self.__b = b

#     def printval(self):
#         print(self.__b)

#     def setval(self, val):
#         self.__b = val


# d = Demo(1, 2)
# # print(d.b)

# d.__b = 10
# d.printval()

# d.setval(10)
# d.printval()


class A:
    def __init__(self):
        self.a = 10

    def display(self):
        print(self.a)


class B(A):
    def __init__(self, name):
        super().__init__()
        self.name = name


b = B('Roshan')
print("Name:", b.name)
print(b.a)
