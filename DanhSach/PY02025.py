n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = list(set(a))
b = list(set(b))
a.sort()
b.sort()
mp1 = {}
mp2 = {}
for i in a:
    mp1[i] = 1
for i in b:
    mp2[i] = 1
for i in a:
    if i in mp2:
        print(i, end = " ")
print()
for i in a:
    if mp2.get(i) is None:
        print(i, end = " ") 
print()
for i in b:
    if mp1.get(i) is None:
        print(i, end = " ")