'''
Из букв слова К А Р К А С составляются 6-буквенные последовательности. Сколько можно составить различных последовательностей, если известно, что в каждой из них содержится не менее 3 согласных?
'''
from itertools import product
k = 0
coll = product('карс', repeat=6)
for w in coll:
    word = ''.join(w)
    if (word.count('к') + word.count('р') + word.count('с')) > 2:
        k += 1
print(k)