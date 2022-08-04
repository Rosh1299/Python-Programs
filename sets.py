# Set
# Unordered collection of unique items
# duplicate values are not allowed
# can not access by index


list1 = [1, 1, 2, 3, 4]
# print(list1)

first = set(list1)
second = {1, 5, 6}

# print(first)
# print(second)

# union
print(first | second)

# intersection
print(first & second)

# difference
print(first - second)
print(second - first)

# symmetric difference

print(first ^ second)

# set comprehensions
s = {x for x in range(10)}
print(s)
