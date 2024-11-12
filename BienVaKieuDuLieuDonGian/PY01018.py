P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    if s[0] == '0':
        break
    k, s = s.split()
    k = int(k)
    ans = ""
    for i in s:
        pos = P.find(i)
        ans += P[(pos + k) % 28]
    print(ans[::-1])