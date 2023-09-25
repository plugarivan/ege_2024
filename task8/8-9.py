'''
Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:

1. ААААА
2. ААААО
3. ААААУ
4. АААОА
...
Запишите слово, которое стоит на 240-м месте от начала списка.

'''
from itertools import product

print([i for i in product('аоу', repeat=5)][239])