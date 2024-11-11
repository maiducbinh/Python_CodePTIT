class SoPhuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, other):
        return SoPhuc(self.a + other.a, self.b + other.b)
    def multiply(self, other):
        return SoPhuc(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    def __str__(self):
        s = f"{self.a}"
        if self.b < 0:
            s += " - " + str(abs(self.b)) + "i"
        else:
            s += " + " + str(self.b) + "i"
        return s
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    sp1 = SoPhuc(a, b)
    sp2 = SoPhuc(c, d)
    print(str((sp1.add(sp2)).multiply(sp1)) + ", " +  str((sp1.add(sp2)).multiply(sp1.add(sp2))))
