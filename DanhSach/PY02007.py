mp = {}
a = []
while True:
    try:
        a += list(map(int, input().split()))
    except:
        break
for i in a:
    mp[i % 42] = 1
print(len(mp))