a = []
b = "02468"
def Try(i):
    s = i
    a.append(int(s + s[::-1]))
    if len(s) < 3:
        for j in b:
            Try(s + j)
for i in b[1:]:
    Try(i)
a.sort()
for _ in range(int(input())):
    n = int(input())
    for i in a:
        if i < n:
            print(i, end = " ")
    print()