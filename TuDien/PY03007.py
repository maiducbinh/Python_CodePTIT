import re
s = ''
while True:
    try:
        s += input().lower() + " "
    except:
        break
s = re.split("[.?!]\s*", s)
s.remove("")
for i in s:
    i = i[0].upper() + i[1:]
    i = i.split()
    print(" ".join(i))