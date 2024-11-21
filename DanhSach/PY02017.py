for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for i in a:
        if i not in mp:
            mp[i] = 1
        else:
            mp[i] += 1
    for i in a:
        if mp[i] % 2 == 1:
            print(i)
            break