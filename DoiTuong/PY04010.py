class ThiSinh:
    def __init__(self, ten, dob, d1, d2, d3):
        self.ten = ten
        self.dob = dob
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tong = d1 + d2 + d3
    def __str__(self):
        return self.ten + " " + self.dob + " " + "{:.1f}".format(self.tong)

ten = input()
dob = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
a = ThiSinh(ten, dob, d1, d2, d3)
print(a)