mp = {}
a = []
for _ in range(int(input())):
    x = input()
    if x != '':
        a.append(x)
        if len(a) == 1:
            mp[a[0]] = 0
        else:
            mp[a[0]] += 1
    else:
        a = []
for i in mp:
    print(f'{i}: {mp[i]}')