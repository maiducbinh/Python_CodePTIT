n = int(input())
a = list(map(int, input().split()))
mn = 2 * 10 ** 6
id = 0
for i in range(n):
    s = 0
    for j in a:
        s += abs(j - a[i])
    if s < mn:
        mn = s
        id = i
print(mn, a[id])