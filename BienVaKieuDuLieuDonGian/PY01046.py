def solve(n, A, B, C):
    if n == 1:
        print(f"{A} -> {C}")
        return
    solve(n - 1, A, C, B)
    print(f"{A} -> {C}")
    solve(n - 1, B, A, C)

n = int(input())
solve(n, 'A', 'B', 'C')