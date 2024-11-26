from math import *
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
mx = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            if a[i][j] > mx and isPrime(a[i][j]):
                mx = a[i][j]
                b = []
                b.append([i, j])
            elif a[i][j] == mx:
                b.append([i, j])
if mx != 0:
    print(mx)
    for i in b:
        print(f'Vi tri {[i[0]]}{[i[1]]}')
else:
    print('NOT FOUND')