a = []
b = ['0', '2', '4', '6', '8']
def Try(s):
    k = s[::-1]
    a.append(int(s + k))
    if len(s) < 3:
        for i in b:
            Try(s + i)
for i in range(1, 5):
    Try(b[i])
a.sort() 
for _ in range(int(input())):
    n = int(input())
    for i in a:
        if i < n:
            print(i, end = ' ')
    print()