'''
Текстовый файл 24-s1.txt состоит не более чем из 10**6 символов и содержит только заглавные буквы латинского алфавита (ABC…Z). Текст разбит на строки различной длины. Необходимо найти строку, содержащую наименьшее количество букв A (если таких строк несколько, надо взять ту, которая в файле встретилась раньше). Определите, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая стоит последней в алфавите. Запишите в ответе эту букву, а затем – сколько раз она встречается во всем файле.
'''
minA = 10 ** 10
for line in open('files/24-s1.txt'):
    countA = line.count('A')
    if countA < minA:
        minA = countA
        s = line
slovar = {}
for x in s:
    slovar[x] = slovar.get(x, 0) + 1
alph = []
for y in slovar.items():
    if y[1] == max(slovar.values()):
        alph.append(y[0])
print(max(alph))
print(open('24-s1.txt').read().count(max(alph)))
