for _ in range(int(input())):
    s = input()
    cnt = 0
    st = []
    for i in s:
        if i == '(':
            cnt += 1
            st.append(cnt)
            print(cnt, end=" ")
        elif i == ')':
            print(st.pop(-1), end = " ")
    print()