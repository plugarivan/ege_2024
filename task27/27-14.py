'''
В файле записана последовательность натуральных чисел. Назовём парой любые два числа из последовательности, расстояние между которыми не менее 15. Расстоянием называется разность номеров элементов последовательности. Необходимо определить количество пар, в которых сумма чисел в паре делится без остатка на 8, а их произведение – на 729.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых в первой строке содержит натуральное число N (1 ≤ N < 1 000 000). В каждой из следующих N строк записано по одному натуральному числу, не превышающему 10 000.
Пример входного файла:
7
81
21
48
74
36
63
78
Будем искать пары с расстоянием между элементами не менее 3. В этой последовательности существует одна пара чисел, 81 и 63, сумма которых (144) делится на 8, а произведение (5103) делится на 729. Ответ: 1.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
'''
with open('files/14/27-137a.txt') as f:
    n = int(f.readline())
    data = [int(i) for i in f]
    count = 0
    for i in range(n - 15):
        for j in range(i + 15, n):
            if (data[i] + data[j]) % 8 == 0 and (data[i] * data[j]) % 729 == 0:
                count += 1
print(count)
def divs3(n):
    d3 = 0
    while n % 3 ** (d3 + 1) == 0 and d3 < 6:
        d3 += 1
    return d3
with open('files/14/27-137b.txt') as f:
    N = int(f.readline())
    pairs = [[0] * (6 + 1) for _ in range(8)]
    ocher = []
    count = 0
    for i in range(N):
        x = int(f.readline())
        if len(ocher) >= 15:
            d = ocher.pop(0)
            r = d % 8
            d3 = divs3(d)
            pairs[r][d3] += 1
        r = x % 8
        r2 = 0 if r == 0 else 8 - r
        d3 = divs3(x)
        count += sum(pairs[r2][6 - d3:6 + 1])
        ocher.append(x)
    print(count)





