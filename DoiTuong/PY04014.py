def xepLoai(d):
    if d >= 9:
        return "XUAT SAC"
    elif d >= 8:
        return "GIOI"
    elif d >= 7:
        return "KHA"
    elif d >= 5:
        return "TB"
    else:
        return "YEU"

class Student:
    def __init__(self, stt, ten, d):
        self.ma = "HS{:02d}".format(stt)
        self.ten = ten
        self.diem = d[0] + d[1]
        for i in d:
            self.diem += i
        self.diem = self.diem / 10 / 1.2
        self.loai = xepLoai(self.diem)
    def __str__(self):
        return self.ma + " " + self.ten + " " + "{:.1f}".format(self.diem) + " " + self.loai

a = []
for i in range(int(input())):
    ten = input()
    d = list(map(float, input().split()))
    a.append(Student(i + 1, ten, d))
a.sort(key=lambda x: (-x.diem, x.ma))
for i in a:
    print(i)