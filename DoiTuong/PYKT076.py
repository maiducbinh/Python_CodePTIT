from datetime import datetime
class TL:
    def __init__(self, stt, ten):
        self.ma = "TL{:03d}".format(stt)
        self.ten = ten
class Phim:
    def __init__(self, stt, tl, ngay, ten, tap):
        self.ma = "P{:03d}".format(stt)
        self.tl = tl
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.ten = ten
        self.tap = tap
    def __str__(self):
        return self.ma + " " + self.tl + " " + self.ngay.strftime("%d/%m/%Y") + " " + self.ten + " " + str(self.tap)
a = []
n, m = map(int, input().split())
for i in range(n):
    a.append(TL(i + 1, input().strip()))
b = []
for i in range(m):
    matl = input().strip()
    tl = ""
    for j in a:
        if j.ma == matl:
            tl = j.ten
            break
    b.append(Phim(i + 1, tl, input().strip(), input().strip(), int(input())))
b.sort(key=lambda x: (x.ngay, x.ten, -x.tap))
for i in b:
    print(i)