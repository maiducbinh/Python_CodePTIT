for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x, y, z = 0, 0, 0
    cnt = 0
    while x < n and y < m and z < k:
        if a[x] == b[y] == c[z]:
            print(a[x], end=' ')
            x += 1
            y += 1
            z += 1
            cnt += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        elif c[z] < a[x]:
            z += 1
    print("NO" if cnt == 0 else "")