'''
(А. Куканова) Лена составляет 5-буквенные слова из букв Я, С, Н, О, В, И, Д, Е, Ц, причём слово должно начинаться с согласной и заканчиваться гласной. Первая и последняя буквы слова встречаются в нем только один раз; остальные буквы могут повторяться. Сколько слов может составить Лена?
'''
from itertools import product

count = 0
for w in product('ясновидец', repeat=5):
    if (w[0] in 'снвдц' and w.count(w[0]) == 1 and w[-1] in 'яоие' and w.count(w[-1]) == 1):
        count += 1
print(count)