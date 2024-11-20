import re
class TS:
    def __init__(self, stt, ten, diem, dt, kv):
        self.ma = "TS{:02d}".format(stt)
        self.ten = normalize(ten)   
        self.diem = diem
        self.dt = dt
        self.kv = kv
        self.tong = cong(kv, dt) + diem
    def __str__(self):
        return self.ma + " " + self.ten + " " + "{:.1f}".format(self.tong) + " " + ("Do" if self.tong >= 20.5 else "Truot")

def normalize(s):
    s = s.strip().lower()
    s = re.split(r'\s+', s)
    return " ".join(i.capitalize() for i in s)
def cong(kv, dt):
    s = 0
    if kv == "1":
        s += 1.5
    elif kv == "2":
        s += 1
    if dt != "Kinh":
        s += 1.5
    return s

a = []
for i in range(int(input())):
    a.append(TS(i+1, input(), float(input()), input(), input()))
a.sort(key=lambda x: -x.tong)
for i in a:
    print(i)