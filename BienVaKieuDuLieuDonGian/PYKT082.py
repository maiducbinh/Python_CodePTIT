def convert(x):
    if x >= 39:
        return 9
    elif x >= 37:
        return 8.5
    elif x >= 35:
        return 8
    elif x >= 33:
        return 7.5
    elif x >= 30:
        return 7
    elif x >= 27:
        return 6.5
    elif x >= 23:
        return 6
    elif x >= 20:
        return 5.5
    elif x >= 16:
        return 5
    elif x >= 13:
        return 4.5
    elif x >= 10:
        return 4
    elif x >= 7:
        return 3.5
    elif x >= 5:
        return 3
    return 2.5

for _ in range(int(input())):
    r, l, s, w = map(float, input().split())
    r = convert(r)
    l = convert(l)
    x = (r + l + s + w) / 4
    if x - int(x) >= 0.75: 
        x = int(x) + 1
    elif x - int(x) >= 0.25: 
        x = int(x) + 0.5
    else: 
        x = int(x)
    print('{:.1f}'.format(x))