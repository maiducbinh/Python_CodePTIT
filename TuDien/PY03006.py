import re
s = ""
for _ in range(int(input())):
    s += input().lower() + " "
a = re.split("[^a-z]", s)
mp = {}
for i in a:
    if i != "":
        if mp.get(i) is None:
            mp[i] = 1
        else:
            mp[i] += 1
a = sorted(mp, key=lambda x: (-mp[x], x))
for i in a:
    print(i, mp[i])
