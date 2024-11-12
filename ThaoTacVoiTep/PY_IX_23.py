def check(a):
    if len(a) <= 2:
        return True
    dx = a[1][0] - a[0][0]
    dy = a[1][1] - a[0][1]
    for i in range(2, len(a)):
        if (a[i][0] - a[0][0]) * dy != (a[i][1] - a[0][1]) * dx:
            return False
    return True

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
if check(a):
    print("No")
else:
    print("Yes")
    for i in range(1, 4):
        print(i, end = " ")