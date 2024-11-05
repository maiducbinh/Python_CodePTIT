import re

for _ in range(int(input())):
    n = int(input())
    s = " " + input().replace(" ", "  ") + " "
    i = -8
    a = []
    while i < 9 and len(a) < 4:
        regex = "\\d" * abs(i) + " "
        if i < 0:
            regex = "-" + regex
        elif i > 0:
            regex = " " + regex
        else:
            i += 1
            continue
        a += [int(x) for x in re.findall(regex, s)]
        i += 1
    ans = 0
    a.sort()
    for x in a[:3]:
        ans += x
    print(ans)