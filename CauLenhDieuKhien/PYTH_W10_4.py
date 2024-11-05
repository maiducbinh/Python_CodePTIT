while True:
    x = int(input())
    if x == -1:
        break
    d = (x + 8) // 9
    print(d * 9)