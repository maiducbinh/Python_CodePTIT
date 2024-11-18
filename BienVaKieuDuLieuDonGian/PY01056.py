from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(s):
    for i in range(0, len(s), 2):
        if int(s[i]) % 2 == 1:
            return False
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0:
            return False
    su = sum([int(i) for i in s])
    return prime(su)
for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")