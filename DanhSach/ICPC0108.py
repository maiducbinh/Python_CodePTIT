for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            if a[i] + a[j] + a[k] == 0:
                cnt += 1
                j += 1
            elif a[i] + a[j] + a[k] < 0:
                j += 1
            else:
                k -= 1
    print(cnt)