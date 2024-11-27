from datetime import datetime

class Mon:
    def __init__(self, ma, ten, hthuc):
        self.ma = ma
        self.ten = ten
        self.hthuc = hthuc
class Ca:
    def __init__(self, stt, ngay, gio, phong):
        self.ma = "C{:03}".format(stt)  
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.phong = phong
class Lich:
    def __init__(self, maca, ngay, gio, phong, mon, nhom, sv):
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.mon = mon
        self.nhom = nhom
        self.sv = sv
        self.maca = maca
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ngay.strftime("%d/%m/%Y"), self.gio.strftime("%H:%M"), self.phong, self.mon, self.nhom, self.sv)
    
f = open("MONTHI.in", "r")
a = []
n = int(f.readline())
for i in range(n):
    ma = f.readline().strip()
    ten = f.readline().strip()
    hthuc = f.readline().strip()
    a.append(Mon(ma, ten, hthuc))
f = open("CATHI.in", "r")
b = []
n = int(f.readline())
for i in range(n):
    ngay = f.readline().strip()
    gio = f.readline().strip()
    phong = f.readline().strip()
    b.append(Ca(i + 1, ngay, gio, phong))
f = open("LICHTHI.in", "r")
c = []
n = int(f.readline())
for i in range(n):
    s = f.readline().strip().split(" ")
    maca = s[0]
    mamon = s[1]
    nhom = s[2]
    sv = s[3]
    mon = ""
    for i in a:
        if i.ma == mamon:
            mon = i.ten
            break
    ngay, gio, phong = "", "", ""
    for i in b:
        if i.ma == maca:
            ngay = i.ngay
            gio = i.gio
            phong = i.phong
            break
    c.append(Lich(maca, ngay, gio, phong, mon, nhom, sv))
c.sort(key = lambda x: (x.ngay, x.gio, x.maca))
for i in c:
    print(i)