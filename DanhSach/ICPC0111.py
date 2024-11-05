for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in (a[d:] + a[0:d]):
        print(i, end=" ")   
    print()