n = (input())
b = 3
while len(n) % 3 != 0:
    n = '0' + n
for i in range(0, len(n), 3):
    tmp = int(n[i]) * 4 + int(n[i + 1]) * 2 + int(n[i + 2])
    print(tmp, end = '')