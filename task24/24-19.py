'''
Текстовый файл 24-211.txt содержит строку из набора A, B, C, D, E, F, всего не более чем из 10**6 символов. Найдите максимальное количество подряд идущих четвёрок символов ABEC, BDAC, CAFB, CFBA, стоящих одна за другой и пересекающихся с соседними четвёрками одной буквой. Например, в строке BDEABECAFBDACBD такие пары составляют подстроку ABECAFBDAC = ABEC + СAFB + ВDAC, итого 3 четвёрки.
'''
s = open('files/24-211.txt').readline()
kmax = k = 0
i = 0
while i < len(s) - 3:
    if s[i:i+4] in ['ABEC', 'BDAC', 'CAFB', 'CFBA']:
        k += 1
        kmax = max(k, kmax)
        i += 2
    else:
        k = 0
    i += 1
print(kmax)