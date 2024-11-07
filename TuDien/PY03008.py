n = int(input())
a = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
a = sorted(a[1:], key=len)
if len(a[-1]) == n - 1:
    print("Yes")
else:
    print("No")
