'''Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1. Перемножаются первая и вторая, а также вторая и третья цифры.
2. Полученные два числа записываются друг за другом в порядке неубывания без разделителей.
Пример. Исходное число: 631. Произведение: 6*3 = 18; 3*1 = 3. Результат: 318. Укажите наибольшее число, при обработке которого автомат выдаёт результат 621.
'''
for x in range(100, 1000):
    s = str(x)
    s1 = int(s[0]) * int(s[1])
    s2 = int(s[1]) * int(s[2])
    if s1 >= s2:
        final = str(s2) + str(s1)
    else:
        final = str(s1) + str(s2)
    if final == '621':
        print(x)

