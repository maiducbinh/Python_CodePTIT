n = int(input())
a = []
while True:
    try:
        a += list(map(int, input().split()))
    except:
        break
o = []
e = []
for i in range(n):
    if a[i] % 2 == 0:
        e.append(a[i])
        a[i] = 0
    else:
        o.append(a[i])
        a[i] = 1
o.sort(key=lambda x: -x)
e.sort()
for i in a:
    if i == 0:
        print(e.pop(0), end=' ')
    else:
        print(o.pop(0), end=' ')
