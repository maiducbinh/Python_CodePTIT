for _ in range(int(input())):
    n, b = map(int, input().split())    
    st = []
    while n != 0:
        st.append(n % b)
        n //= b
    st.reverse()
    for i in st:
        if i < 10:
            print(i, end = '')
        else:
            print(chr(i - 10 + ord('A')), end = '')
    print()