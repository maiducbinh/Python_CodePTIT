for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ok = 1
    for i, j in zip(a, b):
        if i > j:
            ok = 0
            break
    print("YES" if ok else "NO")