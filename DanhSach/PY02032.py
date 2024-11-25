s = input()
a = [int(s[i] + s[i + 1]) for i in range(0, len(s) - 1, 2)]
a = list(set(a))
a.sort()
for i in a:
    print(i, end = " ")