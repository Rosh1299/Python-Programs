# WAP to create following pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
for i in range(1, 6):
    for j in range(1, 6-i):
        print(j, end=' ')
    print()
