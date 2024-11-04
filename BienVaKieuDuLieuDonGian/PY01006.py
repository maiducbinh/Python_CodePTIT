for _ in range(int(input())):
    s = input()
    cnt = 0
    for i in s:
        if i == '4' or i == '7':
            cnt += 1
    print("YES" if cnt == len(s) else "NO")