'''
В файле 17-354.txt содержится последовательность целых чисел, по модулю не превышающих 10000. Определите количество пар элементов последовательности, в которых запись только одного элемента из двух заканчивается цифрой 8, а сумма квадратов элементов пары больше, чем квадрат наибольшего из всех элементов последовательности, запись которых заканчивается цифрой 5. В ответе запишите два числа: сначала количество найденных пар, затем минимальную сумму квадратов элементов этих пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
s = [int(x) for x in open('files/17-354.txt')]
numbers = []
max5 = max(t for t in s if abs(t) % 10 == 5)
for i in range(len(s) - 1):
    if ((abs(s[i]) % 10 == 8) + (abs(s[i + 1]) % 10 == 8)) == 1 and \
                (s[i] ** 2 + s[i + 1] ** 2) > max5 ** 2:
        numbers.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(numbers), min(numbers))
