n = int(input())
a = []
b = []
cnt = 0
for i in range(n):
    s = input().split()
    if i == 0:
        if len(s) == 6:
            a.append(1)
    if len(s) == 6 and len(b) > 0 and len(b[-1]) == 7:
        a.append(1)
    if len(s) == 7:
        cnt += 1
    if cnt == 4:
        a.append(2)
        cnt = 0
    b.append(s)
print(len(a))
for i in a:
    print(i)