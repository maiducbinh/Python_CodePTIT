from math import *
for _ in range(int(input())):
    n = int(input())
    s = "1"
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            s += " * " + str(i)
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            s += "^" + str(cnt)
    if n > 1:
        s += " * " + str(n) + "^1"
    print(s)