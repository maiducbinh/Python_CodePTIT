def dfs(u, a, d):
    d[u] = 1
    for v in a[u]:
        if d[v] == 0:
            dfs(v, a, d)

n = int(input())
m = int(input())
a = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
d = [0] * (n + 1)
dfs(1, a, d)
cnt = 0
for i in range(1, n + 1):
    if d[i] == 1:
        cnt += 1
print("NO" if cnt == n else "YES")