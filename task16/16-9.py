'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n*n + 3*n + 5, при n > 30
F(n) = 2*F(n+1) + F(n+4), при чётных n ≤ 30
F(n) = F(n+2) + 3*F(n+5), при нечётных n ≤ 30
Определите количество натуральных значений n из отрезка [1; 1000], для которых значение F(n) содержит не менее двух значащих цифр 0 (в любых разрядах).
'''
def f(n):
    if n > 30:
        return n * n + 3 * n + 5
    else:
        if n % 2 == 0:
            return 2 * f(n + 1) + f(n + 4)
        else:
            return f(n + 2) + 3 * f(n + 5)


k = 0
for n in range(1, 1001):
    if str(f(n)).count('0') > 1:
        k += 1
print(k)