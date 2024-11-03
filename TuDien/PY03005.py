import re
n, k = map(int, input().split())
mp = {}
for _ in range(n):
    s = input().lower()
    a = re.split("[^0-9a-z]", s)
    for i in a:
        if i == '':
            continue
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
ans = sorted(mp, key=lambda x: (-mp[x], x))
for i in ans:
    if mp[i] >= k:
        print(i, mp[i])