from collections import deque
# using deque to implement queue
def bfs(a, n, m):
    q = deque()
    q.append([0, 0])
    d = [[0] * m for i in range(n)]
    while len(q) > 0:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return d[x][y]
        if y + 1 < m:
            kc = abs(a[x][y] - a[x][y + 1])
            if kc > 0 and y + kc < m and d[x][y + kc] == 0:
                q.append([x, y + kc])
                d[x][y + kc] = d[x][y] + 1
        if x + 1 < n:
            kc = abs(a[x + 1][y] - a[x][y])
            if kc > 0 and x + kc < n and d[x + kc][y] == 0:
                q.append([x + kc, y])
                d[x + kc][y] = d[x][y] + 1
        if x + 1 < n and y + 1 < m:
            kc = abs(a[x + 1][y + 1] - a[x][y])
            if kc > 0 and x + kc < n and y + kc < m and d[x + kc][y + kc] == 0:
                q.append([x + kc, y + kc])
                d[x + kc][y + kc] = d[x][y] + 1
    return -1

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(bfs(a, n, m))