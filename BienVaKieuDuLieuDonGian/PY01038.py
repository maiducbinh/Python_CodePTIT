for _ in range(int(input())):
    n = int(input())
    ok = 0
    for i in range(1000):
        m = int(str(n)[::-1])
        if n % 7 == 0:
            print(n)
            ok = 1
            break
        m = int(str(n)[::-1])
        n += m
    if ok == 0:
        print(-1)