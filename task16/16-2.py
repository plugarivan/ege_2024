'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 2 при n = 1
F(n) = F(n–1) + 5·n2, если n > 1
Чему равно значение функции F(39)?
'''
def f(n):
    if n == 1:
        return 2
    if n > 1:
        return f(n - 1) + 5 * n ** 2

print(f(39))
