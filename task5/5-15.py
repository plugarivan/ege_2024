'''
(В.Н. Шубинкин) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
1) Строится двоичная запись числа N.
2) К этой записи дописывается ещё три или четыре разряда по следующему правилу: если N нечётное, то слева к нему приписывается "1", а справа - "11". В противном случае слева приписывается "11", а справа "00".
Например, N = 510 = 1012 => 1101112 = 5510 = R
Полученная таким образом запись (в ней на три или четыре разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. Укажите наибольшее число R, меньшее 127, которое может быть получено с помощью описанного алгоритма. В ответ запишите это число в десятичной системе счисления.
'''
