'''
Текстовый файл 24-215.txt содержит строку из символов A, B, C и цифр 1, 2, 3, всего не более чем 10**6 символов. Определите максимальное количество идущих подряд троек символов вида «буква + цифра + буква».
'''
s = open('files/24-215.txt').readline()
kmax = k = 0
for j in range(3):
    k = 0
    for i in range(j, len(s)-2, 3):
        if s[i] in 'ABC' and s[i + 1] in '123' and s[i + 2] in 'ABC':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
print(kmax)
