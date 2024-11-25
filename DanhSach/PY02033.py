s = input()
a = [int(s[i] + s[i + 1]) for i in range(0, len(s) - 1, 2)]
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
        print(i, end = ' ')
