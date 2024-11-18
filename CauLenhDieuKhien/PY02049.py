for _ in range(int(input())):
    n, p = map(int, input().split())
    d = 0
    for i in range(1, n + 1):
        while i % p == 0:
            d += 1
            i //= p
    print(d)