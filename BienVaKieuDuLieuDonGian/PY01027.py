def check(s):
    for i in range(len(s)):
        if s[i] not in '68':
            return False
        if i >= 2 and s[i - 2: i + 1] == '888':
            return False
    return True

s = input()
print("YES" if check(s) else "NO")