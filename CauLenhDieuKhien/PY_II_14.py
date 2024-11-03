h, m, s = map(int, input().split())
print("Angle: ", (h % 12) * 30 + m * 30/60 + s * 30/3600)
