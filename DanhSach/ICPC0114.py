from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def check(n):
    s = str(n)
    for i in s:
        if not(prime(int(i))):
            return False
    if prime(n) and prime(sumOfDigits(n)) and prime(int(s[::-1])):
        return True
    return False

for _ in range(int(input())):
    n = int(input())
    print("Yes" if check(n) else "No")