for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for i in a:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    a = sorted(mp, key=lambda x: (-mp[x], x))
    if mp[a[0]] > n // 2:
        print(a[0])
    else:
        print("NO")