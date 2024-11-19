for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    num = len(set(a))
    print((max(a) - min(a) + 1) - num)