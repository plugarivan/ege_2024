'''
В файле 17-205.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов заканчивается на 17, а их сумма делится на 2. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
s = [int(x) for x in open('files/17-205.txt')]
numbers = []
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) % 2 == 0 and (abs(s[i]) % 100 == 17 or abs(s[i + 1]) % 100 == 17):
        numbers.append(s[i] + s[i + 1])
print(len(numbers), max(numbers))
