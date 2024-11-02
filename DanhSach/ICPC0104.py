import re
for _ in range(int(input())):
    s = input()
    a = re.split("[^0-9]", s)
    m = 10 ** 18
    for i in a:
        try:
            m = min(m, int(i))
        except:
            continue
    print(m)