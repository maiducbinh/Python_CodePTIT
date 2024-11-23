x = [0] * 10
dd = [0] * 10
n = 0
s = []
def out():
    for i in range(1, n + 1):
        print(s[x[i] - 1], end = "")
    print()
def Try(i):
    for j in range(1, n + 1):
        if dd[j] == 0:
            x[i] = j
            dd[j] = 1
            if i == n:
                out()
            else:
                Try(i + 1)
            dd[j] = 0       
s = [i for i in input()]
n = len(s)
Try(1)