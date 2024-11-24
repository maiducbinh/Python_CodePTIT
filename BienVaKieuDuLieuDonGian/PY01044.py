a = input().lower().split()
b = input().lower().split()
mp = {}
mp1 = {}
for i in a:
    mp[i] = 1
    mp1[i] = 1
for i in b:
    mp[i] = 1
    if i in mp1 and mp1[i] == 1:
        mp1[i] = 2
for i in sorted(mp):
    print(i, end = ' ')
print()
for i in sorted(mp1):
    if mp1[i] == 2:
        print(i, end = ' ')