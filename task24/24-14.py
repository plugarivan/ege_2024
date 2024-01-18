'''
Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 10**6 символов. Определите максимальное количество идущих подряд символов, среди которых нет точек, а количество гласных (букв A, E, I, O, U, Y) не превышает 7.
'''
s = open('files/24-181.txt').readline()
kmax = 0
for c in 'AEIOUY':
    s = s.replace(c, '*')
for p in s.split('.'):
    res = '*' + p + '*'
    a = [i for i in range(len(res)) if res[i] == '*']
    for i in range(len(a) - 8):
        kmax = max(kmax, a[i + 8] - a[i] - 1)
print(kmax)


