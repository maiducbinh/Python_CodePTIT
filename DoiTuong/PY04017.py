def gio(x):
    t = x.split(":")
    return int(t[0]) + int(t[1]) / 60
class Racer:
    def __init__(self, ten, dv, end):
        self.ten = ten
        self.dv = dv
        self.ma = ""
        for i in dv.split():
            self.ma += i[0]
        for i in ten.split():
            self.ma += i[0]
        self.m = gio(end) - gio("6:00")
        self.v = 120 / self.m
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.dv + " " + str(round(self.v)) + " Km/h"
a = []
for i in range(int(input())):
    a.append(Racer(input(), input(), input()))
a.sort(key=lambda x: (-x.v))
for i in a:
    print(i)