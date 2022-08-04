# unpacking opertor

numbers = [1, 2, 3]
print(numbers)
# * is a unpacking operator to unpack list element as well as tuple and set.
print(*numbers)

values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3, 4]

values = [*first, *"python", *second]
print(values)


# Dictionary

first = {"x": 1, "a": 5}
second = {"y": 3, "z": 4}

combined = {**first, **second}
print(combined)
