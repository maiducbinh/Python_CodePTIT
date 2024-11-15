for _ in range(int(input())):
    s = input()
    a = s[0]
    b = s[1]
    if a == b:
        print("NO")
        continue
    ok = 1
    for i in range(0, len(s), 2):
        if s[i] != a:
            ok = 0
            break
    for i in range(1, len(s), 2):
        if s[i] != b:
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")