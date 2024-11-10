n = int(input())
a = []
for _ in range(n):
    a.append(input())
row = []
col = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][j] == 'C':
           cnt += 1
    row.append(cnt)
for j in range(n):
    cnt = 0
    for i in range(n):
        if a[i][j] == 'C':
            cnt += 1
    col.append(cnt)
ans = 0
for i in range(n):
    ans += row[i] * (row[i] - 1) // 2
    ans += col[i] * (col[i] - 1) // 2
print(ans)