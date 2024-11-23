for _ in range(int(input())):
    s = input()
    s = "".join(sorted(s))
    sum = 0
    t = ""
    for i in s:
        try:
            tmp = int(i)
            sum += tmp
            s.replace(i, "")
        except:
            t += i
    print(t + str(sum))