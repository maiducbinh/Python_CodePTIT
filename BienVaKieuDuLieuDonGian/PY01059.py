for _ in range(int(input())):
    s = input()
    su = sum([int(s[i]) for i in range(0, len(s), 2)])
    print(su, end = " ")
    le = [int(s[i]) for i in range(1, len(s), 2)]
    le.sort()
    if le[0] == le[-1] and le[0] == 0:
        print(0)
    else:
        t = 1
        for i in le:
            if i != 0:
                t *= i
        print(t)