a = []
n = int(input())
for _ in range(n):
    a.append(input())
s = a[0]
m = 2500
ok = 1
l = len(s)
for i in range(l):
    d = 0
    for j in range(n):
        tmp = a[j]
        for k in range(l):
            if tmp == s:
                d += k
                break
            tmp = tmp[1:] + tmp[0]
        if tmp != s:
            ok = 0
    s = s[1:] + s[0]
    m = min(m, d)
if ok:
    print(m)
else:
    print(-1)