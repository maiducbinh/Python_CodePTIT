a0, b0, c0 = map(int, input().split())
a1, b1, c1 = map(int, input().split())
if a0 > a1:
    a1 += 24
print((a1 - a0) * 3600 + (b1 - b0) * 60 + c1 - c0)