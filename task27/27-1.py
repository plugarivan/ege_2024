'''
Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает 1000. Требуется найти для этой последовательности контрольное значение – наибольшее число R, удовлетворяющее следующим условиям:
– R – произведение двух различных переданных элементов последовательности («различные» означает, что не рассматриваются квадраты переданных чисел, произведения различных, но равных по величине элементов допускаются);
– R делится на 7 и не делится на 49.
Если такое произведение получить невозможно, считается, что контрольное значение R = 1.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 10 000.
Пример входного файла:
6
60
17
3
7
9
60
Для указанных входных данных искомое контрольное значение равно 420.
В ответе укажите два числа: сначала контрольное значение для файла А, затем для файла B.
'''
with open('files/1/27-7b.txt') as f:
    max7, maxNo7, = 0, 0
    n = int(f.readline())
    for i in range(n):
        a = int(f.readline())
        if a % 7 != 0 and a > maxNo7:
            maxNo7 = a
        if a % 7 == 0 and a % 49 != 0 and a > max7:
            max7 = a
    if max7 * maxNo7 == 0:
        print(1)
    else:
        print(max7 * maxNo7)
