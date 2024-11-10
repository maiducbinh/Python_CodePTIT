class Mon:
    def __init__(self, ma, ten, thi):
        self.ma = ma
        self.ten = ten
        self.thi = thi
    def __str__(self):
        return f'{self.ma} {self.ten} {self.thi}'

a = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    thi = input()
    a.append(Mon(ma, ten, thi))
a.sort(key=lambda x: x.ma)
for i in a:
    print(i)