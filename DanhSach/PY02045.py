n = input()
while len(n) > 1:
    l = len(n)
    a = int(n[: l//2])
    b = int(n[l//2 :])
    print(a + b)
    n = str(a + b)
    
