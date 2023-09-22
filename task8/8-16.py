'''
(Е. Усов) Леся составляет словосочетания длины 5 из пробела и букв своего имени. При этом никакие две гласные и две согласные не стоят рядом. Словосочетанием считается два слова, разделённых между собой пробелом. Слова не обязательно должны быть осмысленными словами русского языка. Сколько различных словосочетаний может составить Леся?
'''
from itertools import product
k = 0
for x in product(' ЛЕСЯ',repeat=5):
    word = ''.join(x)
    if word[0] != ' ' and word[-1] != ' ' and 'ЛС' not in word and 'СЛ' not in word and 'ЛЛ' not in word\
            and 'СС' not in word and 'ЕЯ' not in word and 'ЯЕ' not in word and 'ЕЕ' not in word \
            and 'ЯЯ' not in word and word.count(' ') == 1:
        k += 1
print(k)