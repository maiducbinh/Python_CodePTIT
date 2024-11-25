s = input()
k = int(input())
a = [int(s[i] + s[i + 1]) for i in range(0, len(s) - 1, 2)]
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1
ok = 0
for i in sorted(mp):
    if mp[i] >= k:
        print(i, mp[i])
        ok = 1
if not ok:
    print("NOT FOUND")