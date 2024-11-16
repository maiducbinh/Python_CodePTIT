n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if i < j:
            s1 += a[i][j]
        else:
            s2 += a[i][j]
if abs(s1 - s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1 - s2))