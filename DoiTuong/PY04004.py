from math import *
class PS:
    def __init__(self, t, m):
        self.t = t
        self.m = m
    def toiGian(self):
        g = gcd(self.t, self.m)
        self.t //= g
        self.m //= g
    def __add__(self, other):
        return PS(self.t * other.m + other.t * self.m, self.m * other.m)
    def __str__(self):
        return f'{self.t}/{self.m}'

t1, m1, t2, m2 = map(int, input().split())
ps1 = PS(t1, m1)
ps2 = PS(t2, m2)
ps3 = ps1 + ps2
ps3.toiGian()
print(ps3)