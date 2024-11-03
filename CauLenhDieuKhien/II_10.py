m = int(input())
v = int(input())
t = int(input())
d = input()
s = v * t
if d == 'C':
    print(s % m)
else:
    if s % m == 0:
        print(0)
    else:
        print(m - s % m)
