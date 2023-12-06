for n in range(3, 10000):
    s = '4' + n * '1'
    while '31' in s or '411' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '411' in s:
            s = s.replace('411', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '4', 1)
    if sum(map(int, s)) == 36:
        print(n)
        break