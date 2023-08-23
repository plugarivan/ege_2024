'''На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Вычисляется сумма S1 всех нечётных цифр десятичной записи числа N. Если нечётных цифр нет, сумма S1 считается равной 0.
2) Вычисляется сумма S2 всех цифр десятичной записи числа N, стоящих в чётных разрядах. Разряды нумеруются справа налево, начиная с 0.
3) Вычисляется результат R как модуль разности S1 и S2.
Например, N = 1234. Сумма нечётных цифр S1 = 1 + 3 = 4. Сумма цифр в чётных разрядах S2 = 2 + 4 = 6. Результат работы алгоритма R = 6 – 4 = 2.
Укажите наименьшее число, в результате обработки которого по данному алгоритму получится число 29.
'''
for n in range(1, 10000000):
    s = str(n)[::-1]
    s1 = sum([int(i)for i in s if int(i) % 2])
    s2 = sum([int(s[i]) for i in range(0, len(s), 2)])
    if abs(s2 - s1) == 29:
        print(n)
        break
