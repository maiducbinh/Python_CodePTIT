for _ in range(int(input())):
    s = input()
    i = 1
    cnt = 1
    last = s[0]
    while i < len(s):
        if s[i] == last:
            cnt += 1
            i += 1
        else:
            print(str(cnt) + last, end = '')
            cnt = 1
            last = s[i]
            i += 1
    print(str(cnt) + last)
    