n = int(input())
a = []
for i in range(n - 1):
    a.append(int(input()))
a.sort()
i = 1
for j in a:
    if i == j:
        i += 1
        continue
    else:
        print(i)
        break