from datetime import datetime

class Mon:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
class Lich:
    def __init__(self, stt, mon, tg, nhom):
        self.ma = "T{:03d}".format(stt)
        self.mon = mon
        self.tg = datetime.strptime(tg, "%d/%m/%Y %H:%M")
        self.nhom = nhom
    def __str__(self):
        return self.ma + " " + self.mon.ma + " " + self.mon.ten + " " + self.tg.strftime("%d/%m/%Y %H:%M") + " " + self.nhom
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(Mon(input(), input()))
b = []
for i in range(m):
    s = input().split()
    tg = s[1] + " " + s[2]
    for j in a:
        if j.ma == s[0]:
            b.append(Lich(i + 1, j, tg, s[3]))
            break
b.sort(key=lambda x: (x.tg, x.ma))
for i in b:
    print(i)