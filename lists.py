# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Go to the editor
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True


# list1 = [19, 19, 5, 5, 5, 5, 5]
# if list1.count(19) == 2 and list1.count(5) >= 3:
#     print("True")
# else:
#     print('False')

# age = 22
# if 18 <= age <= 65:
#     print('eligible')

# count = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#         count += 1
# else:
#     print(f"we have {count} even numbers")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))


# list unpacking

numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)

numbers = [1, 2, 3, 4, 5, 6]
first, second, *other = numbers
print(first, second, other)

# Looping over list
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)


# Sorting the list
numbers = [3, 4, 53, 67, 5]
# numbers.sort(reverse=True)
print(sorted(numbers))
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 50),
    ("Product3", 20),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# lambda function
items.sort(key=lambda item: item[1])
print(items)
