'''
Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 7 цифр, причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import permutations
k = 0
for x in permutations('0123456789', r=7):
    numb = ''.join(x)
    if all(int(numb[i]) % 2 != int(numb[i + 1]) % 2 for i in range(len(numb) - 1)) and numb[0] != '0' and numb[-1] in '05':
        k += 1
print(k)