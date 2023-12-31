'''На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. Укажите минимальное число N, после обработки которого автомат получает число, большее 138. В ответе это число запишите в десятичной системе.
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0: s += '01'
    else: s += '10'
    if int(s, 2) > 138:
        print(n)
        break