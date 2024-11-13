f = [0] * 100
def init():
    f[1] = 1
    f[2] = 1
    for i in range(3, 93):
        f[i] = f[i - 1] + f[i - 2]
for _ in range(int(input())):
    a, b = map(int, input().split())
    init()
    for i in range(a, b + 1):
        print(f[i], end=' ')
    print()