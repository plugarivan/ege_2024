'''
Текстовый файл 24-197.txt содержит строку из заглавных латинских букв X, Y и Z, всего не более чем из 10**6 символов. Определите максимальное количество идущих подряд троек символов X*Y или Z*Y, где * обозначает один любой символ.
'''
s = open('files/24-197.txt').readline()
kmax =  0
for j in range(3):
    k = 0
    for i in range(j, len(s)-2, 3):
        if s[i:i+3] in ('XZY','XXY','XYY', 'ZYY','ZXY','ZZY'):
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)


