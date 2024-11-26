for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(float, input().split())
        a.append((x, y))
    dp = [1] * (n + 5)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][0] < a[j][0] and a[i][1] > a[j][1]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(max(dp))