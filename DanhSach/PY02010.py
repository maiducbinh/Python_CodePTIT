while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for _ in range(n):
        a.append(int(input()))
    mi = min(a)
    mx = max(a)
    if mi == mx:
        print("BANG NHAU")
    else:
        print(f'{mi} {mx}')