'''
Сколько существует чисел, шестнадцатеричная запись которых содержит 3 цифры, причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.'''
from itertools import permutations
k = 0
for x in permutations('0123456789abcdef', r=3):
    numb = ''.join(x)
    if all(int(numb[i], 16) % 2 != int(numb[i + 1], 16) % 2 for i in range(len(numb) - 1)) and numb[0] != '0':
        k += 1
print(k)