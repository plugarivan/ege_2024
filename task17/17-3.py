'''
(А. Кабанов) В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно. Рассматривается множество элементов последовательности, которые удовлетворяют следующим условиям:
− сумма цифр числа кратна 5;
− троичная запись числа не заканчивается на 00.
Найдите количество таких чисел и наибольший из них.
'''
def three(a):
    thr = ''
    while a:
        thr += str(a % 3)
        a //= 3
    return thr[::-1]


s = [int(x) for x in open('files/17-4.txt')]
numbers = []
for i in s:
    if sum(map(int, str(i))) % 5 == 0 and three(i)[-2:] != '00':
        numbers.append(i)
print(len(numbers), max(numbers))

