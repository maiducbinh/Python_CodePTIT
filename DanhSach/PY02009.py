for _ in range(int(input())):
    mp = {}
    n = int(input())
    for i in range(n):
        x = int(input())
        if mp.get(x) == None:
            mp[x] = 1
        else:
            mp[x] += 1
    a = sorted(mp, key=lambda x: (-mp[x], x))
    print(a[0])