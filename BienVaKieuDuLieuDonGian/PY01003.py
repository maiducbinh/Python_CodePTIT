for _ in range(int(input())):
    s = list(input())
    n = len(s)
    # print(len(s))
    while len(s) > 1:
        if int(s[-1]) >= 5:
            c = int(s[-2]) + 1
            s[-2] = str(c)
        s.pop(-1)
    print(s[0] + "0" * (n - 1))