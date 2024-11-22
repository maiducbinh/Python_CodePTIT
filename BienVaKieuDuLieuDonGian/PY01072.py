n, k = 0, 0
a = []
x = [0] * 25
def Try(i):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            out()
        else:
            Try(i + 1)
def out():
    for i in range(1, k + 1):
        print(a[x[i] - 1], end = " ")
    print()
n, k = map(int, input().split())
a = list(map(int, input().split()))

a = list(set(a))
a.sort()
n = len(a)
Try(1)
