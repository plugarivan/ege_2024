'''Дана программа для исполнителя Редактор:

НАЧАЛО
  ПОКА нашлось (56) ИЛИ нашлось (3333)
    заменить (56, 3)
    заменить (3333, 3)
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 121 строки 563 (563563563…563)?
'''
s = 121 * '563'
while '56' in s or '3333' in s:
    s = s.replace('56', '3', 1)
    s = s.replace('3333', '3', 1)
print(s)