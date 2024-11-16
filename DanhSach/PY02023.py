def f(x):
    a = str(x)
    a = [int(i) for i in a]
    return sum(a)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (f(x), x))
    for i in a:
        print(i, end=' ')
    print()
    