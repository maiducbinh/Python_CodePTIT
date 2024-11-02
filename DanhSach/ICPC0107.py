for _ in range(int(input())):
    p, q = input().split()
    s = input()
    if len(s.split()) == 2:
        x, y = s.split()
    else:
        x = s
        y = input()
    if p > q:
        p, q = q, p
    a = x.replace(q, p) 
    b = y.replace(q, p)
    c = x.replace(p, q)
    d = y.replace(p, q)
    print(int(a) + int(b), int(c) + int(d))