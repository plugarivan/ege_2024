'''(А. Игнатюк) Исполнитель «Аппо» получает на вход четырехзначное число N и строит новое число R по следующим правилам:
1) Если первая цифра числа N делится на 4, то заменяем её на цифру 9.
2) Если первая цифра числа N делится на 2 и не делится на 4, то заменяем её на цифру 3.
Сколько существует чисел N, для которых соответствующее число R начинается с цифры 9, а восьмеричная запись числа R оканчивается цифрой 4?
'''
k = 0
for n in range(1000, 10000):
    s = str(n)
    if int(s[0]) % 4 == 0: s = '9' + s[1:]
    if int(s[0]) % 2 == 0 and int(s[0]) % 4 != 0: s = '3' + s[1:]
    if s[0] == '9' and oct(int(s))[-1] == '4':
        k += 1
print(k)