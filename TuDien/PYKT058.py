def dfs(i, v, x, a, d):
    d[i] = 1
    for j in a[i]:
        if d[j] == 0 and j != x:
            dfs(j, v, x, a, d)
for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    a = [[] for i in range(n + 5)]
    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
    cnt = 0
    for i in range(1, n + 1):
        if i != u and i != v:
            d = [0] * (n + 5)
            dfs(u, v, i, a, d)
            if d[v] == 0:
                cnt += 1
    print(cnt)
