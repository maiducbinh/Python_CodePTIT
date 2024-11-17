for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    for i in range(n):
        if len(st) == 0:
            st.append(i)
            print(i + 1, end = " ")
        else:
            while len(st) > 0 and a[i] >= a[st[-1]]:
                st.pop(-1)
            if len(st) == 0:
                print(i + 1, end = " ")
            else:
                print(i - st[-1], end = " ")
            st.append(i)
    print()
