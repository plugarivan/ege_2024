'''Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 99 единиц?

НАЧАЛО
  ПОКА нашлось (111)
    заменить (111, 22)
    заменить (222, 11)
  КОНЕЦ ПОКА
КОНЕЦ
'''
s = 99 * '1'
while '111' in s:
    s = s.replace('111', '22', 1)
    s = s.replace('222', '11', 1)
print(s)