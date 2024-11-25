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
b = []
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
        b.append(i)
n = len(b)
for i in range(1, n):
    b[i] += b[i - 1]
idx = -1
for i in range(n):
    if prime(b[i]) and prime(b[-1] - b[i]):
        idx = i
        break 
print("NOT FOUND" if idx == -1 else idx)