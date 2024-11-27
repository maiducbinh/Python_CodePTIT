def palin(s):
    return s == s[::-1]

f = open("VANBAN.in", "r")
mp = {}
for i in f:
    s = i.split()
    for j in s:
        if not palin(j):
            continue
        if j not in mp:
            mp[j] = 1
        else:
            mp[j] += 1
a = sorted(mp, key = lambda x: -len(x))
for i in a:
    if len(i) == len(a[0]):
        print(i, mp[i])