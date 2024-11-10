def check(a, op, b, c):
    if op == '+':
        return a + b == c
    if op == '-':
        return a - b == c
    if op == '*':
        return a * b == c
    if op == '/':
        if b == 0:
            return False
        return a // b == c and a % b == 0
    return False

def genOp(a):
    if a == '?':
        return ['+', '-', '*', '/']
    return [a]

def genNum(a):
    if a[0] == '?':
        if a[1] == '?':
            return [str(i) for i in range(10, 100)]
        return [str(i) + a[1] for i in range(1, 10)]
    else:
        if a[1] == '?':
            return [a[0] + str(i) for i in range(10)]
        return [a]

def solve(s):
    a = s.split()
    x = genNum(a[0])
    op = genOp(a[1])
    y = genNum(a[2])
    z = genNum(a[4])
    for i in x:
        for j in op:
            for k in y:
                for l in z:
                    if check(int(i), j, int(k), int(l)):
                        print('{} {} {} = {}'.format(i, j, k, l))
                        return
    print("WRONG PROBLEM!")

for _ in range(int(input())):
    solve(input())