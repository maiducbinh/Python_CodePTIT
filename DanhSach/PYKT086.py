from math import *
x = '0123456789ABCDEF'
f = open('E:\\Nam4_Ky1\\Python\\Code\\DanhSach\\DATA.in', 'r')
for i in range(int(f.readline())):
    n = int(f.readline())
    s = f.readline()[:-1] #delete \n
    if n == 2:
        print(s)
        continue
    b = int(log2(n))
    while len(s) % b != 0:
        s = '0' + s
    ans = ""
    for i in range(0, len(s), b):
        p = 1
        sum = 0
        for j in range(i + b - 1, i - 1, -1):
            sum += int(s[j]) * p
            p *= 2
        print(x[sum], end="")
    print()