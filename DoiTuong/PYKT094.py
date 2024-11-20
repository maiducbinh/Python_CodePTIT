class Phong:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
def heSo(nhom, nam):
    if nhom == 'A':
        if 1 <= nam <= 3:
            return 10
        elif 4 <= nam <= 8:
            return 12
        elif 9 <= nam <= 15:
            return 14
        else:
            return 20
    elif nhom == 'B':
        if 1 <= nam <= 3:
            return 10
        elif 4 <= nam <= 8:
            return 11
        elif 9 <= nam <= 15:
            return 13
        else:
            return 16
    elif nhom == 'C':
        if 1 <= nam <= 3:
            return 9
        elif 4 <= nam <= 8:
            return 10
        elif 9 <= nam <= 15:
            return 12
        else:
            return 14
    else:
        if 1 <= nam <= 3:
            return 8
        elif 4 <= nam <= 8:
            return 9
        elif 9 <= nam <= 15:
            return 11
        else:
            return 13
class NV:
    def __init__(self, ma, ten, phong, luong, ngay):
        self.ma = ma
        self.ten = ten
        self.phong = phong
        self.luong = luong
        self.ngay = ngay
        self.outcome = luong * ngay * heSo(ma[0], int(ma[1:3]))
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.phong + " " + str(self.outcome) + "000"
n = int(input())
a = []
for i in range(n):
    s = input().split()
    a.append(Phong(s[0], " ".join(s[1:])))
m = int(input())
b = []
for i in range(m):
    ma = input()
    for j in a:
        if j.ma == ma[-2:]:
            b.append(NV(ma, input(), j.ten, int(input()), int(input())))
            break
for i in b:
    print(i)
