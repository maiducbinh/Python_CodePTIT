n = int(input()) + 1
a = list(map(int, input().split()))
a.append(-1)
mx = max(a)
ans = 0
l = 0
for i in range(n):
    if a[i] == mx:
        l += 1
    else:
        ans = max(ans, l)
        l = 0
print(ans)