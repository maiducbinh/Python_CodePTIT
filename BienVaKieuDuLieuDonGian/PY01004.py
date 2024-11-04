from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(0, n):
        if gcd(n, i) == 1:
           cnt += 1
    print("YES" if prime(cnt) else "NO")