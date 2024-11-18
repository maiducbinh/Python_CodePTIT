from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(s):
    if not prime(len(s)):
        return False
    cnt = 0
    for i in s:
        if prime(int(i)):
            cnt += 1
    return cnt > len(s) - cnt
for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")