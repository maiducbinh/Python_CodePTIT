x = [0] * 20
n, k = 0, 0
a = []
def Try(i):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            for l in range(1, k + 1):
                print(a[x[l] - 1], end = " ")
            print()
        else:
            Try(i + 1)

n, k = map(int, input().split())
a = input().split()
a = list(set(a))
a.sort()
n = len(a)
Try(1)