n = int(input())
a = []
while True:
    try:
        a.extend(list(map(int, input().split())))
    except:
        break
i = 1
mx = max(a)
ok = 1
for i in range(1, mx):
    if i not in a:
        print(i)
        ok = 0
if ok == 1:
    print("Excellent!")