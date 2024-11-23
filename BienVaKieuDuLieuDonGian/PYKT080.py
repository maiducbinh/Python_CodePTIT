dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
cnt = 0
dd = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < m and dd[x][y] == 0:
                    cnt += a[x][y]
                    dd[x][y] = 1
print(cnt)