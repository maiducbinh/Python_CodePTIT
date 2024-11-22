f = open("DATA.in", 'r')
a = []
for i in f.readlines():
    s = i.split()
    for j in s:
        try:
            num = int(j)
            if len(j) > 9:
                a.append(j)
        except:
            a.append(j)
a.sort()
for i in a:
    print(i, end = " ")
