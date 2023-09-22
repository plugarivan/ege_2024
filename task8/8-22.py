'''
*Рассматриваются числа, восьмеричная запись которых содержит ровно 11 знаков. Определите количество таких чисел, в восьмеричной записи которых ровно четыре нечётных цифры, причём никакие две нечётные цифры не стоят рядом.
'''
from itertools import product

k = 0
for w in product('cn', repeat=11):
    w = ''.join(w)
    if w.count('n') == 4 and 'nn' not in w:
        if w[0] == 'c':
            k += 3 * 4 ** 10
        else:
            k += 4 ** 11
print(k)