n = int(input())
for i in range(n):
    for j in range(n - i, n):
        print(j, end=' ')
    for j in range(0, n - i):
        print(j, end = " ")
    print()