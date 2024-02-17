'''
(П. Финкель) Текстовый файл 24-230.txt состоит не более чем из 10**6 символов и содержит буквы английского алфавита и цифры. Определите максимальное число в этом файле, ограниченное двумя парами символов ZZ и удовлетворяющее маске «8???54???22», где символ ? обозначает любую цифру. Пример такого числа: 81235412322. Найдите произведение нечётных цифр найденного числа.
'''
from fnmatch import fnmatch

res = []
s = open('files/24-230.txt').readline()
for x in s.split('ZZ'):
    if fnmatch(x, '8???54???22'):
        res.append(x)
pr = 1
if max(res).isdigit():
    for i in max(res):
        if int(i) % 2:
            pr *= int(i)
print(pr)