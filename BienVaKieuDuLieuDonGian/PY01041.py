for _ in range(int(input())):
    s = input()
    if len(s) < 3:
        print("NO")
        continue
    idx = len(s)
    for i in range(0, len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            idx = i
            break
    ok = 1
    for i in range(0, idx):
        if int(s[i]) >= int(s[i + 1]):
            ok = 0
            break
    for i in range(idx, len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            ok = 0
            break
    print("YES" if ok else "NO")