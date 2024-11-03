class SV:
    def __init__(self, ten, c, t):
        self.ten = ten
        self.c = c
        self.t = t
    def __str__(self):
        return self.ten + " " + str(self.c) + " " + str(self.t) 
a = []
for _ in range(int(input())):
    ten = input()
    c, t = map(int, input().split())
    a.append(SV(ten, c, t))
a.sort(key=lambda x: (-x.c, x.t, x.ten))
for i in a:
    print(i)