s1 = s2 = 0
for x in range(1, 1000):
    s1 += (x - 1) * x
    s2 += x + 1
    if s1 + 2 * s2 > 3300000:
        print(x - 1)
        break
