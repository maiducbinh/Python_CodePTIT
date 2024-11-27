import re
n = int(input())
a = []
for _ in range(n):
    s = input()
    s = re.sub("[^0-9]", " ", s)
    try:
        for i in s.split():
            a.append(int(i))
    except:
        continue
a.sort()
for i in a:
    print(i)