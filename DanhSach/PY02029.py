n, m = map(int, input().split())
a = list(map(int, input().split()))
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1
a.sort(key=lambda x: (-mp[x], x))
if mp[a[0]] == mp[a[-1]]:
    print("NONE")
else:
    i = 1
    while mp[a[i]] == mp[a[0]]:
        i += 1
    print(a[i])