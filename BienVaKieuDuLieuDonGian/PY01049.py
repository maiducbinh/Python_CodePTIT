from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    n = input()
    if not prime(int(len(n))):
        print("NO")
        continue
    cnt = 0
    for i in n:
        if prime(int(i)):
            cnt += 1
    if cnt > len(n) - cnt:
        print("YES")
    else:
        print("NO")