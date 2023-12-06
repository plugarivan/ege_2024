'''Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 3, если n < 3,
F(n) = 2n + 5 + F(n-2), если n ≥ 3.
Чему равно значение выражения F(3027) – F(3023)?
'''
import sys

sys.setrecursionlimit(10000)


def f(n):
    if n < 3: return 3
    else:
        return 2 * n + 5 + f(n - 2)


print(f(3027) - f(3023))