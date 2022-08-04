
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = sorted(list1, reverse=True)

for x, y in zip(list1, sorted(list1, reverse=True)):
    if x != y:
        print(x, "+", y, "=", x+y)
    else:
        print(x, "=", y, "=", x)


# list3 = list(map(lambda x, y: x+y if x != y else x, list1, list2))
# print(list3)
