n = int(input())
a = list(map(int, input().split()))
sum = -10 ** 9
s = 0
st = 0
e = 0
for i in range(n):
    s += a[i]
    if s > sum:
        sum = s
        e = i
    if s < 0:
        s = 0
        st = i + 1
print(st + 1, e + 1, sum)