def dfs(u, a, d):
    d[u] = 1
    for v in a[u]:
        if d[v] == 0:
            dfs(v, a, d)
n, m, x = map(int, input().split())
a = [[] for i in range(n + 5)]
for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
d = [0] * (n + 5)
dfs(x, a, d)
cnt = 0
for i in range(1, n + 1):
    if d[i] == 0:
        print(i)
        cnt += 1
if cnt == 0:
    print('0')