'''На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
1. Строится троичная запись числа N.
2. Если число N делится на 3, к троичной записи справа дописываются две её последние цифры, иначе остаток от деления числа на 3 умножается на 5, переводится в троичную систему и дописывается в конец троичной записи.
3. Полученная таким образом запись является троичной записью искомого числа R.
Например, для числа 11 троичная запись 1023 преобразуется в запись 1021013 = 307, для числа 12 троичная запись 1103 преобразуется в 110103 = 111. Укажите минимальное значение R, большее чем 133, которое может быть результатом работы алгоритма.
'''
def three(x):
    t = ''
    while x:
        t += str(x % 3)
        x //= 3
    return t[::-1]

l = []
for n in range(1, 100):
    s = three(n)
    if n % 3 == 0: s += s[-2:]
    else: s += three((n % 3) * 5)
    if int(s, 3) > 133:
        l.append(int(s, 3))
print(min(l))
