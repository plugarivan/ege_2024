'''Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (111)
  заменить (111, 22)
  заменить (222, 11)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка содержала более 50 единиц и не содержала других цифр. Укажите минимально возможную длину исходной строки, при которой в результате работы этой программы получится строка, содержащая минимально возможное количество единиц.
'''
minim = 10 ** 10
for i in range(51, 100):
    s = i * '1'
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    if s.count('1') < minim:
        minim = s.count('1')
        m = i
print(m)