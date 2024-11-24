c = '012'
a = []
def Try(s, cnt):
    if cnt > len(s) - cnt:
        a.append(s)
    if len(s) <= 10:
        Try(s + '0', cnt)
        Try(s + '1', cnt)
        Try(s + '2', cnt + 1)
Try("1", 0)
Try("2", 1)
a = [int(i) for i in a]
a.sort()
# for i in a:
#     print(i)
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(a[i], end = ' ')
    print()