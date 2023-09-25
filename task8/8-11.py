'''
Все 5-буквенные слова, составленные из букв А, З, Н, С, записаны в алфавитном порядке и пронумерованы. Вот начало списка:

1. ААААА
2. ААААЗ
3. ААААН
4. ААААС
5. АААЗА
...
Какое количество слов находятся между словами САЗАН и ЗАНАС (включая эти слова)?

'''
from itertools import product
s = [''.join(i) for i in product('азнс', repeat=5)]
print(s.index('сазан') - s.index('занас') + 1)