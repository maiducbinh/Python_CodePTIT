def dfs(i, x, v, a, d):
    d[x] = 1
    for j in a[x]:
        if j != i and d[j] == 0: 
            dfs(i, j, v, a, d)
for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    a = [[] for _ in range(n + 5)]
    d = [0] * (n + 5)
    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
    cnt = 0
    for i in range(1, n + 1):
        if i != u and i != v:
            d = [0] * (n + 5)
            dfs(i, u, v, a, d)
            if d[v] == 0:
                cnt += 1
    print(cnt)