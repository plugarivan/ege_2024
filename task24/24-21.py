'''
Текстовый файл 24-241.txt состоит не более чем из 10**6 символов и содержит только латинские буквы A, B, C, D, E, F, O. Определите максимальное количество идущих подряд групп символов вида «гласная + гласная + согласная».
'''
s = open('files/24-241.txt').readline()
kmax = k = 0
i = 0
while i < len(s) - 2:
    if s[i] in 'AEO' and s[i + 1] in 'AEO' and s[i + 2] in 'BCDF':
        k += 1
        kmax = max(k, kmax)
        i += 3
    else:
        k = 0
        i += 1
print(kmax)
