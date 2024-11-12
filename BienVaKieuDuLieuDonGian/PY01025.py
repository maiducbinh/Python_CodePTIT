n = input()
n = n[::-1]
cnt = 0
ans = ""
for i in n:
    if cnt == 3:
        ans += ','
        cnt = 0
    ans += i
    cnt += 1
print(ans[::-1])