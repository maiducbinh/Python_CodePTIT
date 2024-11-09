def check(s):
    for i in range(0, len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True
for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")