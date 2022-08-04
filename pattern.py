# Pattern - 1

"""
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    for sp in range(n-i):
        print(" ", end=" ")
    for sp in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

for i in range(1, n+1):
    for j in range(i, n):
        print("*", end=" ")
    for sp in range(i):
        print(" ", end=" ")
    for sp in range(i):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    print()
"""

# Pattern - 2
"""
n = 5
for i in range(1, n+1):
    for sp in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for j in range(i-1):
        print("*", end=" ")
    print()

for i in range(1, n+1):
    for sp in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    for k in range(i, n-1):
        print("*", end=" ")
    print()
"""

# Pattern-3
"""
n = 5
for i in range(1, n+1):
    # loop for LHS spaces
    for sp in range(n-i):
        print(" ", end=" ")
    # loop for printing LHS star
    for j in range(1):
        print("*", end=" ")
    # condition for straight line through
    if i == 3:
        for k in range(n):
            print("*", end=" ")
    else:
        # loop for middle spaces
        for p in range(i-1):
            print(" ", end=" ")
        for sp in range(i-1):
            print(" ", end=" ")
        # loop for printing right hand side star
        for k in range(1):
            print("*", end=" ")
    print()
"""
# Pattern-4

"""n = 5
count = 1
for i in range(1, n+1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()"""


n = 5
for i in range(1, n+1):
    num = 65
    for j in range(i):
        print(chr(num), end=" ")
        num += 1
    print()
