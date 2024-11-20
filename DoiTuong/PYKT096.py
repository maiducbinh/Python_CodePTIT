class Team:
    def __init__(self, stt, ten, uni):
        self.ma = "Team{:02d}".format(stt)
        self.ten = ten
        self.uni = uni
class TS:
    def __init__(self, stt, ten, team, uni):
        self.ma = "C{:03d}".format(stt)
        self.ten = ten
        self.team = team
        self.uni = uni
    def __str__(self):
        return "{} {} {} {}".format(self.ma, self.ten, self.team, self.uni)
n = int(input())
a = []
for i in range(n):
    ten = input()
    uni = input()
    a.append(Team(i + 1, ten, uni))
m = int(input())
b = []
for i in range(m):
    ten = input()
    mateam = input()
    for j in a:
        if j.ma == mateam:
            b.append(TS(i + 1, ten, j.ten, j.uni))
            break
b.sort(key=lambda x: x.ten)
for i in b:
    print(i)    