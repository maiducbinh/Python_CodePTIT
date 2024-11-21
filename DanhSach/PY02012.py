n = int(input())
a = []
while True:
    try:
        a += list(map(int, input().split()))
    except:
        break
e = []
o = []
for i in a:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
o.sort(reverse=True)
e.sort()
for i in a:
    if i % 2 == 0:
        print(e.pop(0), end=' ')
    else:
        print(o.pop(0), end=' ')