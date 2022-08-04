
"""
        *
       * *
      * * *
"""
n = 5
for i in range(1, n+1):
    for sp in range(i, n):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
