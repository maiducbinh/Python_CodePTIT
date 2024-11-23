from math import *
for _ in range(int(input())):
    n, b = map(int, input().split())
    a = []
    while n != 0:
        a.append(n % b)
        n //= b
    a.reverse()
    for i in a:
        if i < 10:
            print(i, end='')
        else:
            print(chr(i + ord('A') - 10), end="")
    print()