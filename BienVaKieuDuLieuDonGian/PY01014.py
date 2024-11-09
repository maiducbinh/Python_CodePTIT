a, k, n = map(int, input().split())
t = k - (a % k)
if a + t > n:
    print(-1)
else:
    for i in range(a + t, n + 1, k):
        print(i - a, end = ' ')