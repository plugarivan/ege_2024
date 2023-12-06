def f(x, p):
    if x >= 205 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 5, p + 1) or f(x * 4, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 5, p + 1) and f(x * 4, p + 1)


print([i for i in range(1, 205) if f(i, 0)])