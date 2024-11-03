a = list(input().split())
a = sorted(a, key=lambda x: len(x))
print(a[-1], len(a[-1]))
    