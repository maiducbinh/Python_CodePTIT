def sumOfDigits(n):
    su = sum([ord(i) - ord('0') for i in n])
    return su

n = input()
cnt = 0
while len(n) > 1:
    n = str(sumOfDigits(n))
    cnt += 1
print(cnt)
