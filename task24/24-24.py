'''
(П.Е. Финкель) Текстовый файл 24-1.txt состоит не более чем из 10**6 символов - заглавных латинских букв и цифр. Определите максимальное число, состоящее только из нечётных цифр. Под числом подразумевается последовательность цифр, ограниченная другими символами (не цифрами).
'''
s = open('files/24-1.txt').readline().strip()
for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    s = s.replace(c, '*')
maxim = 0
for x in s.split('*'):
    if x != '':
        if all(int(i) % 2 for i in x):
            maxim = max(maxim, int(x))
print(maxim)
