from math import *
def palin(s):
    return len(s) > 1 and s == s[::-1]
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
mx = 0
for i in range(n):
    for j in range(m):
        if palin(str(a[i][j])) and a[i][j] > mx:
            mx = a[i][j]
if mx == 0:
    print("NOT FOUND")
else:
    print(mx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == mx:
                print(f"Vi tri [{i}][{j}]")