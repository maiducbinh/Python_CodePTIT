for _ in range(int(input())):
    s = input()
    su = sum([int(s[i]) for i in range(1, len(s), 2)])
    t = 1
    for i in range(0, len(s), 2):
        if s[i] != '0':
            t *= int(s[i])
    print(t, su)