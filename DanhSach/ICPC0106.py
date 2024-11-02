from math import *

def calc(x, p):
    pow = 0
    sum = 0
    while pow < p:
        sum += int(x[p - pow - 1]) * (2 ** pow)
        pow += 1
    return sum
d = 'ABCDEF'
for _ in range(int(input())):
    b = int(input())
    s = input()
    if b == 2:
        print(s)
        continue
    p = int(log2(b))
    while len(s) % p != 0:
        s = "0" + s
    ans = []
    for i in range(0, len(s), p):
        c = calc(s[i: i + p], p)
        if c < 10:
            # ans.append(str(c))
            print(str(c), end="")
        else:
            # ans.append(d[c - 10])
            print(d[c - 10], end="")
    print()