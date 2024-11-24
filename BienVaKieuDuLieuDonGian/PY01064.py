def solve(n, k):
    if k == 2 ** (n - 1):
        return n
    elif k > 2 ** (n - 1):
        return solve(n - 1, k - 2 ** (n - 1))
    else:
        return solve(n - 1, k)
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(chr(solve(n, k) - 1 + ord('A')))