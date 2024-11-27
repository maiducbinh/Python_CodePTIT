from datetime import datetime
class Thi:
    def __init__(self, stt, ngay, gio, phong):
        self.ma = "C{:03}".format(stt)  
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.phong = phong
    def __str__(self):
        return "{} {} {} {}".format(self.ma, self.ngay.strftime("%d/%m/%Y"), self.gio.strftime("%H:%M"), self.phong) 
a = []
f = open("CATHI.in", "r")
n = int(f.readline())
for i in range(n):
    ngay = f.readline().strip()
    gio = f.readline().strip()
    phong = f.readline().strip()
    a.append(Thi(i + 1, ngay, gio, phong))
a.sort(key = lambda x: (x.ngay, x.gio, x.ma))
for i in a:
    print(i)