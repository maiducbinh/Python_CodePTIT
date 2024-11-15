for _ in range(int(input())):
    s = input()
    if all(c in ['0', '1', '2'] for c in s):
        print("YES")
    else:
        print("NO")