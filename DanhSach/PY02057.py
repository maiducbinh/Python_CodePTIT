n, m = map(int, input().split())
a = []
mx = 0
mn = 10 ** 6
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
    mx = max(max(x), mx)
    mn = min(min(x), mn)
d = mx - mn
b = []
for i in range(n):
    for j in range(m):
        if a[i][j] == d:
            b.append([i, j])
if len(b) == 0:
    print('NOT FOUND')  
else:
    print(d)
    for i in b:
        print(f'Vi tri {[i[0]]}{[i[1]]}')