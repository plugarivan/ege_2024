'''
В системе счисления с некоторым основанием p выполняется равенство

    y3y + y65 = x2z0
Буквами x, y и z обозначены некоторые цифры из алфавита системы счисления с основанием p. Запишите в ответе значение числа xyzp в десятичной системе счисления.

'''
'''for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y * p ** 2 + 3 * p + y) + (y * p ** 2 + 6 * p + 5) == (x * p ** 3 + 2 * p ** 2 + z * p):
                    print(x, y, z, p)

print(int('17a', 12))'''

def f(a, n):
  return sum(a[::-1][i] * n ** i for i in range(len(a)))


for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if f([y, 3, y], p) + f([y, 6, 5], p) == f([x, 2, z, 0], p):
                    print(p, x, y, z, f([x, y, z], p))
                    break



