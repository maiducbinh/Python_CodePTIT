def palin(n):
    s = str(n)
    if len(s) < 2:
        return False
    return s == s[::-1]

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
mx = 0
for i in range(n):
    for j in range(m):
        if mx < a[i][j] and palin(a[i][j]):
            mx = a[i][j]
            b = []
            b.append([i, j])
        elif mx == a[i][j] and palin(a[i][j]):
            b.append([i, j])
if mx != 0:
    print(mx)
    for i in b:
        print(f'Vi tri {[i[0]]}{[i[1]]}')
else:
    print('NOT FOUND')