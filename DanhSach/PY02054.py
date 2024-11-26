n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
row = []
col = []
if n > m:
    d = n - m
    for i in range(0, d * 2, 2):
        row.append(i)
elif m > n:
    d = m - n
    for i in range(1, d * 2 + 1, 2):
        col.append(i)
for i in range(n):
    if i in row:
        continue
    for j in range(m):
        if j not in col:
            print(a[i][j], end=' ')
        else:
            continue
    print()