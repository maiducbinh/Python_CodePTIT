def dfs(u, a, d):
    d[u] = 1
    for v in a[u]:
        if d[v] == 0:
            dfs(v, a, d)
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[] for i in range(n + 5)]
    for i in range(m):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    mx = 0
    idx = 0
    for i in range(1, n + 1):
        d = [0] * (n + 5)
        cnt = 0
        d[i] = 1
        for j in range(1, n + 1):
            if d[j] == 0:
                cnt += 1
                dfs(j, a, d)
        if mx < cnt:
            mx = cnt
            idx = i
    if mx == 1:
        print(0)
    else:
        print(idx)