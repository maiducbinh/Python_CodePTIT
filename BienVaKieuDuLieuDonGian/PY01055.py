def check(s):
    if s[0] == s[1]:
        return False
    if len(s) % 2 == 0:
        return False
    for i in range(0, len(s), 2):
        if s[i] != s[0]:
            return False
    return True
for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")