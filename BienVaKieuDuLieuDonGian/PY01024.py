def check(s):
    a = sum([int(i) for i in s])
    if a % 10 != 0:
        return False
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            return False
    return True
for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")  
