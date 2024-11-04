from math import *
class PS:
    def __init__(self, t, m):
        self.t = t
        self.m = m

    def toiGian(self):
        g = (gcd(self.t, self.m))
        self.t //= g
        self.m //= g
    
    def __str__(self):
        return '{}/{}'.format(self.t, self.m)

t, m = map(int, input().split())
ps = PS(t, m)
ps.toiGian()
print(ps)