'''
Операнды арифметического выражения записаны в системе счисления с основанием 19:

    98x7964119 + 36х1419 + 73x419
В записи чисел переменной x обозначена неизвестная цифра из алфавита 19-ричной системы счисления. Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 18. Для найденного значения x вычислите частное от деления значения арифметического выражения на 18 и укажите его в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.

'''
alph = '0123456789ABCDEFGHI'
for x in alph:
    f = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if f % 18 == 0:
        print(f // 18)
