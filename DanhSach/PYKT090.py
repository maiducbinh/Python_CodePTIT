a = []
f = open("CONTACT.in", "r")
for i in f:
    x = i.lower()
    if x not in a:
        a.append(x)
a.sort()
for i in a:
    print(i)