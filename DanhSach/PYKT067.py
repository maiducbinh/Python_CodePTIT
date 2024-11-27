n = 0
x = [0] * 15
dd = [0] * 15
a = []
def Try(i):
    for j in range(1, n + 1):
        if dd[j] == 0:
            x[i] = j
            dd[j] = 1
            if i == n - 1:
                s = ""
                for i in range(n):
                    s += str(x[i])
                a.append(s)
            else:
                Try(i + 1)
            dd[j] = 0
        
for _ in range(int(input())):
    n = int(input())
    a = []
    Try(0)
    a.sort(reverse=True)
    print(len(a))
    for i in a:
        print(i, end = " ")
    print()