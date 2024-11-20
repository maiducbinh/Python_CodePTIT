import re

def normalize(s):
    s = s.lower().strip()
    s = re.split(r'\s+', s)
    return " ".join(i.capitalize() for i in s)
def muc(loai):
    if loai == 'A':
        return 100
    elif loai == 'B':
        return 500
    return 200
class KH:
    def __init__(self, stt, ten, loai, dau, cuoi):
        self.ma = "KH{:02d}".format(stt)
        self.ten = normalize(ten)
        self.loai = loai
        self.dau = dau
        self.cuoi = cuoi
        self.muc = muc(loai)
        self.trong = 0
        self.ngoai = 0
        self.vat = 0
        if cuoi - dau <= self.muc:
            self.trong = (cuoi - dau) * 450
        else:
            self.trong = self.muc * 450
            self.ngoai = (cuoi - dau - self.muc) * 1000
            self.vat = self.ngoai // 20
        self.tong = self.trong + self.ngoai + self.vat
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.trong, self.ngoai, self.vat, self.tong)
a = []
for _ in range(int(input())):
    ten = input()
    s = input().split()
    loai = s[0]
    dau = int(s[1])
    cuoi = int(s[2])
    a.append(KH(_ + 1, ten, loai, dau, cuoi))
a.sort(key=lambda x: -x.tong)
for i in a:
    print(i)