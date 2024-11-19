n = int(input())
a = []
for i in range(n):
    a.append(input())
row = [0] * n
col = [0] * n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            row[i] += 1
            col[j] += 1
ans = 0
for i in range(n):
    ans += row[i] * (row[i] - 1) // 2
    ans += col[i] * (col[i] - 1) // 2
print(ans)