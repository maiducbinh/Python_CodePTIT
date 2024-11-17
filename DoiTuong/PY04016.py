from datetime import datetime
def gia(phong):
    f = phong[0]
    if f == "1":
        return 25
    elif f == "2":
        return 34
    elif f == "3":
        return 50
    return 80
class KH:
    def __init__(self, stt, ten, phong, st, end, phi):
        self.ma = "KH{:02d}".format(stt)
        self.ten = ten
        self.phong = phong
        self.st = datetime.strptime(st, "%d/%m/%Y")
        self.end = datetime.strptime(end, "%d/%m/%Y")
        self.ngay = (self.end - self.st).days + 1
        self.phi = phi
        self.tong = self.ngay * gia(self.phong) + self.phi
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.phong + " " + str(self.ngay) + " " + str(self.tong)    

a = []
for i in range(int(input())):
    a.append(KH(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
a.sort(key=lambda x: -x.tong)
for i in a:
    print(i)