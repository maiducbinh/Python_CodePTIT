class SV:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.cc = 0
        self.thi = ""
    def getCc(self, cc):
        self.cc = 10
        for i in cc:
            if i == "x":
                continue
            elif i == "m":
                self.cc -= 1
            else:
                self.cc -= 2
        if self.cc < 0:
            self.cc = 0
    def getThi(self):
        if self.cc == 0:
            self.thi = "KDDK"
    def __str__(self):
        self.getThi()
        return self.ma + " " + self.ten + " " + self.lop + " " + str(self.cc) + " " + self.thi
a = []
n = int(input())
for _ in range(n):
    a.append(SV(input(), input(), input()))
for _ in range(n):
    t = input().split()
    for i in a:
        if i.ma == t[0]:
            i.getCc(t[1])
for i in a:
    print(i)