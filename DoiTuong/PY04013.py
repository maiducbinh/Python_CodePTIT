from datetime import datetime

def calculate(h):
    s = h.split(":")
    return int(s[0]) * 60 + int(s[1])
 
class Tram:
    def __init__(self, stt, ten, st, e, mua):
        self.ma = "T{:02d}".format(stt)
        self.ten = ten
        self.st = datetime.strptime(st, "%H:%M")
        self.e = datetime.strptime(e, "%H:%M")
        # self.st = calculate(st)
        # self.e = calculate(e)
        self.mua = mua
        # self.tg = self.e - self.st
        self.tg = int((self.e - self.st).total_seconds() / 60)
    def updateTG(self, st, e):
        # st = calculate(st)
        # e = calculate(e)
        st = datetime.strptime(st, "%H:%M")
        e = datetime.strptime(e, "%H:%M")
        # self.tg += self.e - self.st
        self.tg += int((e - st).total_seconds() / 60)
    def updateMua(self, mua):
        self.mua += mua
    def __str__(self):
        return self.ma + " " + self.ten + " " + "{:.2f}".format(self.mua / self.tg * 60)

a = []
cnt = 1
for _ in range(int(input())):
    ten = input()
    st = input()
    e = input()
    mua = (int(input()))
    ok = 0
    for i in a:
        if i.ten == ten:
            i.updateTG(st, e)
            i.updateMua(mua)
            ok = 1
            break
    if ok == 0:
        a.append(Tram(cnt, ten, st, e, mua))
        cnt += 1
for i in a:
    print(i)

