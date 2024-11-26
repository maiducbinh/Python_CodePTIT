for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
    a.sort(key=lambda x: x[1])
    l = 1
    lst = a[0][1]
    for i in range(1, n):
        if a[i][0] >= lst:
            l += 1
            lst = a[i][1]
    print(l)