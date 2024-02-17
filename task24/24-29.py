'''
Текстовый файл 24-s1.txt состоит не более чем из 10**6 заглавных латинских букв (A..Z). Текст разбит на строки различной длины. Определите количество строк, в которых буква S встречается столько же раз, сколько и буква X.
'''
k = 0
for s in open('files/24-s1.txt'):
    if s.count('S') == s.count('X'):
        k += 1
print(k)