'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(1) = G(1) = 1
F(n) = 2·F(n–1) + G(n–1) – 2n, если n > 1
G(n) = F(n–1) +2·G(n–1) + n, если n > 1
Чему равно значение F(14) + G(14)?
'''
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + g(n - 1) - 2 * n

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 * g(n - 1) + n

print(f(14) + g(14))
