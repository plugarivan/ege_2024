'''
Маша составляет коды из букв, входящих в слово РУСЛАН. Каждая буква должна входить в код ровно один раз. Все возможные коды Маша записывает в алфавитном порядке и нумерует. Начало списка выглядит так:
1. АЛНРСУ
2. АЛНРУС
3. АЛНСРУ
...
Какой код будет записан под номером 442?

'''
from itertools import permutations

print([i for i in permutations('алнрсу')][441])