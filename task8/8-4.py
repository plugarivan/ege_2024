'''
Артур составляет 6-буквенные коды перестановкой букв слова ВОРОТА. При этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Артур?
'''
from itertools import permutations
k = set()
coll = permutations('ворота')
for w in coll:
    word = ''.join(w)
    if 'оо' not in word and 'оа' not in word and 'ао' not in word:
        k.add(word)
print(len(k))