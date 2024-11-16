n = int(input())
a = list(map(float, input().split()))
a.sort()
s = 0
cnt = 0
for i in a:
    if i != a[0] and i != a[-1]:
        s += i
        cnt += 1
print("{:.2f}".format(s / cnt))
