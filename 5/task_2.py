for i in range(1000, 10000):
    a, b, c, d = map(int, str(i))
    
    s1 = a + b
    s2 = c + d

    sums = [s1, s2]

    sums.sort()
    result = "".join(str(x) for x in sums)

    if result == '117':
        print(i)


