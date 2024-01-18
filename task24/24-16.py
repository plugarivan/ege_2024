'''
Текстовый файл 24-191.txt содержит строку из заглавных латинских букв, всего не более чем из 10**6 символов. Определите количество подстрок длиной не более 12 символов, которые начинаются и заканчиваются буквой A и не содержат других букв A (кроме первой и последней) и букв B.
'''
s = open('files/24-191.txt').readline()
k = 0
if s[0] != 'A': k -= 1
if s[-1] != 'A': k -= 1
for pod in s.split('A'):
    if len(pod) <= 10 and 'B' not in pod:
        k += 1
print(k)
