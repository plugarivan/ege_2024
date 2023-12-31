'''
Дано арифметическое выражение:

    x321111 + 17x4211
В записи чисел переменной x обозначена неизвестная цифра из допустимого алфавита для указанных систем счисления. Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 111. Для найденного значения x вычислите частное от деления значения арифметического выражения на 111 и укажите его в ответе в десятичной системе счисления.

'''
for x in range(111):
    f1 = x * 111 ** 3 + 3 * 111 ** 2 + 2 * 111 + 1
    f2 = 211 ** 3 + 7 * 211 ** 2 + x * 211 + 4
    if (f1 + f2) % 111 == 0:
        print((f1 + f2) // 111)