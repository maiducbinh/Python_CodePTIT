s = '2357'
a = []
n = 0
def Try(st, c2, c3, c5, c7):
    if c2 > 0 and c3 > 0 and c5 > 0 and c7 > 0 and st[-1] != '2':
        a.append(st)
    if len(st) < n:
        for i in s:
            Try(st + i, c2 + (i == '2'), c3 + (i == '3'), c5 + (i == '5'), c7 + (i == '7'))
n = int(input())
Try('', 0, 0, 0, 0)
a = [int(i) for i in a]
a.sort()
for i in a:
    print(i)