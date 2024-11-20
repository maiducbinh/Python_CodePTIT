import re
from math import *
def normalize(s):
    s = s.strip()
    s = re.split(r'\s+', s)
    return " ".join(i.capitalize() for i in s)
class SV:
    def __init__(self, stt, ten, d1, d2, d3):
        self.ma = "SV{:02d}".format(stt)
        self.ten = normalize(ten)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3 
        self.tb = (d1 * 3 + d2 * 3 + d3 * 2) / 8
    def __str__(self):
        return self.ma + " " + self.ten + " " + "{:.2f}".format(ceil(self.tb * 100) / 100)
a = []
for i in range(int(input())):
    a.append(SV(i + 1, input(), float(input()), float(input()), float(input())))
a.sort(key=lambda x: -x.tb)
print(a[0], 1)
xh = 1
for i in range(1, len(a)):
    if a[i].tb == a[i - 1].tb:
        print(a[i], str(xh))
    else:
        xh = i + 1
        print(a[i], str(xh))
    