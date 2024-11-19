for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    M = max(a)
    for i in range(n):
        if a[i] == M:
            a.insert(i, m)
            break
    a.sort(key=lambda x: (x // (abs(x) + 1)))
    for i in a:
        print(i, end=" ")
    print()