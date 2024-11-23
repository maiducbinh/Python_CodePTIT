for _ in range(int(input())):
    s = input()
    s = s.split('.')
    ok = 1
    if len(s) != 4:
        print('NO')
        continue
    for i in s:
        try:
            if 0 <= int(i) <= 255:
                continue
            else:
                ok = 0
                break
        except:
            ok = 0
            break
    print('YES' if ok else 'NO')