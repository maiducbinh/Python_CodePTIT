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
    n = int(s[-4:])
    if prime(n):
        print("YES")
    else:
        print("NO")