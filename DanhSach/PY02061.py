for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(3):
        b.append(list(map(int, input().split())))
    sum = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            s = 0
            for u in range(-1, 2):
                for v in range(-1, 2):
                    s += a[i + u][j + v] * b[u + 1][v + 1]
            sum += s
    print(sum)