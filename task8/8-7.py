'''
Петя составляет 6-буквенные слова из букв К, О, М, Е, Т, А. Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов может составить Петя?
'''
from itertools import permutations
k = 0
coll = permutations('комета')
for w in coll:
    word = ''.join(w)
    s = ''
    for i in word:
        if i in 'оеа': s += 'g'
        else: s += 's'
    if 'gg' not in s and 'ss' not in s:
        k += 1
print(k)