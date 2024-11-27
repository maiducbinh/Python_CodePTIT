n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i, j in zip(a, b):
    c.append((i, j))
c.sort(key = lambda x: x[0] - x[1])
ans = 0
for i in range(k):
    ans += c[i][0]
i = k
while i < n and c[i][0] < c[i][1]:
    ans += c[i][0]
    i += 1
while i < n:
    ans += c[i][1]
    i += 1
print(ans)