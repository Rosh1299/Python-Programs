items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 20),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# lambda function
items.sort(key=lambda item: item[1])
print(items)


# map function
prices = list(map(lambda item: item[1], items))

# list comprehensions
prices = [item[1] for item in items]
print(prices)

# filter function
filtered_prices = list(filter(lambda item: item[1] >= 10, items))

# list comprehensions
filtered_prices = [item for item in items if item[1] >= 10]
print(filtered_prices)


# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2, "abc")))

print(dict(zip(list1, list2)))


def addition(*num):
    output = 0
    for i in num:
        output += i
    print(output)


def subtraction(*num):
    output = 0
    for i in num:
        output = abs(output-i)
    print(output)


def multiplication(*num):
    output = 1
    for i in num:
        output *= i
    print(output)


def division(*num):
    output = 1
    for i in num:
        output = output/i
    print(output)


division(34, 10, 5)
