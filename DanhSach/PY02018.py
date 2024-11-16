n = int(input())
a = list(map(int, input().split()))
k = 1
a.sort()
for i in range(1, 30001):
    if i not in a:
        print(i)
        break