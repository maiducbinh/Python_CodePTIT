from collections import deque
mp = {}
def init():
    q = deque()
    q.append(1)
    mp[1] = 1
    while len(q) > 0:
        t = q.popleft()
        if t > 10 ** 19:
            break
        # needing conditions
        if t * 2 <= 10 ** 19 and t * 2 not in mp:
            mp[t * 2] = 1
            q.append(t * 2)
        if t * 3 <= 10 ** 19 and t * 3 not in mp:
            mp[t * 3] = 1
            q.append(t * 3)
        if t * 5 <= 10 ** 19 and t * 5 not in mp:
            mp[t * 5] = 1
            q.append(t * 5)
init()
a = sorted(mp)
cnt = 1
for i in a:
    mp[i] = cnt
    cnt += 1
for _ in range(int(input())):
    n = int(input())
    if n in mp:
        print(mp[n])
    else:
        print("Not in sequence")