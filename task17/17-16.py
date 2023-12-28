'''
В файле 17-370.txt содержится последовательность целых чисел, по модулю не превышающих 20000. Определите количество пар элементов последовательности, в которых
– только одно число четырёхзначное;
– сумма квадратов элементов пары делится нацело на максимальное трёхзначное число в последовательности, сумма цифр которого оканчивается на 3.
В ответе запишите сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар. Под парой элементов подразумеваются два соседних элемента последовательности.
'''
s = [int(i) for i in open('files/17-370.txt')]
numbers = []
max3 = max(t for t in s if sum(map(int, str(abs(t)))) % 10 == 3 and 100 <= abs(t) <= 999)
for i in range(len(s) - 1):
    if ((1000 <= abs(s[i]) <= 9999) + (1000 <= abs(s[i + 1]) <= 9999)) == 1 and \
                (s[i] ** 2 + s[i + 1] ** 2) % max3 == 0:
        numbers.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(numbers), max(numbers))
