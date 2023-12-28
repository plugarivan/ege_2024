'''
В файле 17-379.txt содержится последовательность натуральных чисел. Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. Определите количество троек последовательности, в которых только одно из чисел является четырёхзначным, а сумма элементов тройки не меньше максимального элемента последовательности, оканчивающегося на 15. В ответе запишите количество найденных троек, затем максимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
s = [int(i) for i in open('files/17-379.txt')]
numbers = []
max15 = max(t for t in s if t % 100 == 15)
for i in range(len(s) - 2):
    ch = range(1000, 10000)
    if ((s[i] in ch) + (s[i + 1] in ch) + (s[i + 2] in ch)) == 1 and \
        sum(s[i:i+3]) >= max15:
        numbers.append(sum(s[i:i+3]))
print(len(numbers), max(numbers))