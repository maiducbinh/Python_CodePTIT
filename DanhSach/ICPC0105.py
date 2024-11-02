import re
for _ in range(int(input())):
    s = input()
    a = re.split("[^0-9]", s)
    m = 0
    for i in a:
        try:
            m = max(int(i), m)
        except:
            continue
    print(m)