gt = [1] * 11
for i in range(1, 10):
    gt[i] = gt[i - 1] * i
for _ in range(int(input())):
    n = int(input())
    s = str(n)
    sum = 0
    for i in s:
        sum += gt[(int(i))]
    if sum == n:
        print("Yes")
    else:
        print("No")