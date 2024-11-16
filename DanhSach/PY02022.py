from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
mp = {}
for i in a:
    if prime(i):
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
for i in mp:
    print(i, mp[i])