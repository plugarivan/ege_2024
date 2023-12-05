def f(x, y):
    return (x < 4) or (x >= 20) or (y >= 3 * x + a) or (y < 100)


for a in range(1000, -1, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break