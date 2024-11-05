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
    y, z = map(int, s.split())
    sum = sumOfDigits(y)
    print(z // sum)