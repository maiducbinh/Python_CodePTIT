while True:
    x = int(input())
    if x == -1:
        break
    print("YES" if x % 11 == 0 else "NO")