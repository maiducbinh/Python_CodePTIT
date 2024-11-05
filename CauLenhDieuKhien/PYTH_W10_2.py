def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum
while True:
    s = input()
    if s[0] == '-':
        break
    n, h = map(int, s.split())
    cnt = 0
    for i in range(n):
        if sumOfDigits(i) == h:
            cnt += 1
    print(cnt)