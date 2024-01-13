'''
Текстовый файл 24-157.txt состоит не более чем из 10**6 символов и содержит только заглавные буквы латинского алфавита (A..Z). Определите максимальное количество идущих подряд символов, среди которых нет сочетания символов QW.
'''
s = open('files/24-157.txt').readline()
k = kmax = 1
for i in range(len(s) - 1):
    if s[i] == 'Q' and s[i + 1] == 'W':
        k = 1
    else:
        k += 1
        kmax = max(k, kmax)
print(kmax)
