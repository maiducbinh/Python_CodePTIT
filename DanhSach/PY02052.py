n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
s1, s2 = 0, 0
for i in range(n):
    for j in range(0, i):
        s1 += a[i][j]
    for j in range(i + 1, n):
        s2 += a[i][j]
d = abs(s1 - s2)
print("YES" if d <= k else "NO")
print(d)