'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 2*n*n*n + n*n, при n > 25
F(n) = F(n+2) + 2*F(n+3), при n ≤ 25
Определите сумму цифр значения F(2).
'''
def f(n):
    if n > 25:
        return 2 * n * n * n + n * n
    else:
        return f(n + 2) + 2 * f(n + 3)


print(sum(map(int, str(f(2)))))