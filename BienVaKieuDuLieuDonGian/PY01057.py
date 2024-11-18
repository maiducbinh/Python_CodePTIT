from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    s = input()
    ok = 1
    for i in range(len(s)):
        if prime(i) and not prime(int(s[i])):
            ok = 0
        if not prime(i) and prime(int(s[i])):        
            ok = 0
    print("YES" if ok else "NO")