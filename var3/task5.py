def chet(a):
    ch = ''
    while a:
        ch += str(a % 4)
        a //= 4
    return ch[::-1]


for n in range(1, 1000):
    s = chet(n)
    if n % 4 == 0: s += s[-2:]
    else: s += chet(n % 4 * 2)
    if int(s, 4) >= 1025:
        print(n)
        break