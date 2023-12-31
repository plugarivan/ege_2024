'''
В файле 17-354.txt содержится последовательность целых чисел, по модулю не превышающих 10000. Определите количество пар, для которых выполняются следующие условия:
– запись элементов пары заканчивается одной и той же цифрой;
– только один из элементов пары делится без остатка на 3;
– сумма квадратов элементов пары не превышает квадрат наименьшего из всех элементов последовательности, запись которых заканчивается цифрой 1.
В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму элементов этих пар.
'''
s = [int(x) for x in open('files/17-354.txt')]
numbers = []
min1 = min(t for t in s if abs(t) % 10 == 1)
for i in range(len(s) - 1):
    if ((abs(s[i]) % 10) == (abs(s[i + 1]) % 10)) and \
            ((s[i] % 3 == 0) + (s[i + 1] % 3 == 0)) == 1 and \
                (s[i] ** 2 + s[i + 1] ** 2) <= min1 ** 2:
        numbers.append(s[i] + s[i + 1])
print(len(numbers), max(numbers))
