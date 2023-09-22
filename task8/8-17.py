from itertools import permutations
k = 0
for w in permutations('гераклит', r=6):
    s = ''
    for c in w:
        if c in 'грклт': s += 's'
        else: s += 'g'
    if s.count('s') > s.count('g') and 'gg' not in s:
        k += 1
print(k)