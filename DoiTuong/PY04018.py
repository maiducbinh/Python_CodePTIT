def mon(ma):
    if ma[0] == "A":
        return "TOAN"
    elif ma[0] == "B":
        return "LY"
    elif ma[0] == "C":
        return "HOA"
def cong(ma):
    if ma[1] == "1":
        return 2
    elif ma[1] == "2":
        return 1.5
    elif ma[1] == "3":
        return 1
    return 0
class GV:
    def __init__(self, stt, ten, maxt, tin, cm):
        self.ma = "GV{:02d}".format(stt)
        self.ten = ten
        self.mon = mon(maxt)
        self.tong = tin * 2 + cm + cong(maxt)
        if self.tong >= 18:
            self.kq = "TRUNG TUYEN"
        else:
            self.kq = "LOAI"
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.mon + " " + "{:.1f}".format(self.tong) + " " + self.kq
a = []
for i in range(int(input())):
    a.append(GV(i + 1, input(), input(), float(input()), float(input())))
a.sort(key=lambda x: -x.tong)
for i in a:
    print(i)
        