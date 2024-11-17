def loai(d):
    if d < 5:
        return "TRUOT"
    elif d < 8:
        return "CAN NHAC"
    elif d <= 9.5:
        return "DAT"
    return "XUAT SAC"
class TS:
    def __init__(self, stt, ten, lt, th):
        self.ma = "TS0" + str(stt)
        self.ten = ten
        self.lt = lt if lt <= 10 else lt / 10
        self.th = th if th <= 10 else th / 10
        self.tb = (self.lt + self.th) / 2
        self.loai = loai(self.tb)
    def __str__(self):
        return self.ma + " " + self.ten + " {:.2f}".format(self.tb) + " " + self.loai
    
a = []
for i in range(int(input())):
    a.append(TS(i + 1, input(), float(input()), float(input())))
a.sort(key = lambda x: -x.tb)
for i in a:
    print(i)