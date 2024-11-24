for _ in range(int(input())):
    s = input()
    n = len(s)
    p = -1
    for i in range(n - 2, -1, -1):
        if s[i] > s[i + 1]:
            p = i
            break
    if p == -1:
        print(-1)
        continue
    q = p + 1
    t = '0'
    for i in range(p + 1, n):
        if s[i] > t and s[i] > s[p + 1] and s[i] < s[p]:
            t = s[i]
            q = i
    s = s[:p] + s[q] + s[p + 1:q] + s[p] + s[q + 1:]
    if s[0] == '0':
        print(-1)
        continue
    print(s)