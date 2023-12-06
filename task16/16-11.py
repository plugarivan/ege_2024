'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n*n + 5*n + 4, при n > 30
F(n) = F(n+1) + 3*F(n+4), при чётных n ≤ 30
F(n) = 2*F(n+2) + F(n+5), при нечётных n ≤ 30
Определите количество натуральных значений n из отрезка [1; 1000], для которых сумма цифр значения F(n) равна 27.
'''
def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    else:
        if n % 2 == 0:
            return f(n + 1) + 3 * f(n + 4)
        else:
            return 2 * f(n + 2) + f(n + 5)


print(len([n for n in range(1, 1001) if sum(map(int, str(f(n)))) == 27]))