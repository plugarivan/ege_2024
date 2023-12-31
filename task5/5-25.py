'''Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1) Если исходное число кратно 3, оно делится на 3, иначе из него вычитается 1.
2) Если полученное на предыдущем шаге число кратно 7, оно делится на 7, иначе из него вычитается 1.
3) Если полученное на предыдущем шаге число кратно 11, оно делится на 11, иначе из него вычитается 1.
4) Число, полученное на шаге 3, считается результатом работы алгоритма.
Сколько существует различных натуральных чисел N, при обработке которых получится R = 6?
'''
k = 0
for n in range(2, 10000):
    if n % 3 == 0: r = n // 3
    else: r = n - 1
    if r % 7 == 0: r = r // 7
    else: r -= 1
    if r % 11 == 0: r = r // 11
    else: r -= 1
    if r == 6:
        k += 1
print(k)