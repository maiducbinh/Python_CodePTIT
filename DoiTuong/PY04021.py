def gio(x):
    t = x.split(":")
    return int(t[0]) * 60 + int(t[1])

class Gamer:
    def __init__(self, ma, ten, st, end):
        self.ma = ma
        self.ten = ten
        self.st = gio(st)
        self.end = gio(end)
        self.m = self.end - self.st
    def __str__(self):
        return self.ma + " " + self.ten + " " + str(self.m // 60) + " gio " + str(self.m % 60) + " phut"

a = []
for i in range(int(input())):
    a.append(Gamer(input(), input(), input(), input()))
a.sort(key=lambda x: (-x.m))
for i in a:
    print(i)
