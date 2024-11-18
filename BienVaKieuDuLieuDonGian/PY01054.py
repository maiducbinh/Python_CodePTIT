for _ in range(int(input())):
    n = input()
    t = 1
    for i in n:
        if i != '0':
            t *= int(i)
    print(t)