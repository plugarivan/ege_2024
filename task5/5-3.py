'''На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописывается (дублируется) последняя цифра.
3) Затем справа дописывается 0, если в двоичном коде числа N чётное число единиц, и 1, если нечётное.
4) К полученному результату дописывается ещё один бит чётности так, чтобы количество единиц в двоичной записи полученного числа стало чётным.
Полученная таким образом запись (в ней на три разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. Укажите минимальное число R, большее 80, которое могло получиться в результате работы автомата. В ответе это число запишите в десятичной системе.
'''
for n in range(1, 100):
    s = bin(n)[2:]
    s += s[-1]
    if bin(n).count('1') % 2 == 0: s += '0'
    else: s += '1'
    if s.count('1') % 2 == 0: s += '0'
    else: s += '1'
    if int(s, 2) > 80:
        print(int(s, 2))
        break