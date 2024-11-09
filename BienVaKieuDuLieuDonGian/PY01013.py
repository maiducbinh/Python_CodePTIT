from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    s = str(g)
    sum = 0
    for i in s:
        sum += int(i)
    if prime(sum):
        print('YES')
    else:
        print('NO')