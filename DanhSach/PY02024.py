def f(x):
    a = [int(i) for i in str(x)]
    t = 1
    for i in a:
        t *= i
    return t
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (f(x), x))
    for i in a:
        print(i, end=' ')
    print()
    