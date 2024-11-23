for _ in range(int(input())):
    s = input()
    t = input()
    s = "".join(sorted(s))
    t = "".join(sorted(t))
    if s == t:
        print(f"Test {_ + 1}: YES")
    else:
        print(f"Test {_ + 1}: NO")