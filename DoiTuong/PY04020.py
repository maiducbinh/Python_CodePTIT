class MH:
    def __init__(self, ma, ten, sl, gia, ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.ck = ck
        self.tong = sl * gia - ck
    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.gia} {self.ck} {self.tong}"
    
a = []
for i in range(int(input())):
    a.append(MH(input(), input(), int(input()), int(input()), int(input())))
a.sort(key=lambda x: (-x.tong))
for i in a:
    print(i)
    