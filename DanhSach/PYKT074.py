for _ in range(int(input())):
    s = input()
    i = 99
    if len(s) <= 100:
        print(s)
        continue
    while s[i] != ' ' and s[i + 1] != ' ':
        i -= 1
    print(s[:i + 1])