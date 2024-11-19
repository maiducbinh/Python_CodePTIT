def phi(ghe):
    if ghe == 5:
        return 10000
    elif ghe == 7:
        return 15000
    elif ghe == 2:
        return 20000
    elif ghe == 29:
        return 50000
    return 70000    
mp = {}
for _ in range(int(input())):
    a = input().split()
    if a[-2] == "IN":
        if a[-1] not in mp:
            mp[a[-1]] = 0
        mp[a[-1]] += phi(int(a[-3]))
for i in mp:
    print(f"{i}: {mp[i]}")