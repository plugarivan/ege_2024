'''
В файле записана последовательность натуральных чисел. Назовём парой любые два числа из последовательности. Необходимо определить количество пар, в которых сумма чисел в паре делится без остатка на 7, а их произведение – на 2592.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых в первой строке содержит натуральное число N (1 ≤ N < 1 000 000). В каждой из следующих N строк записано по одному натуральному числу, не превышающему 10 000.
Пример входного файла:
7
144
102
137
70
182
11
108
В этой последовательности существует одна пара чисел, 144 и 108, сумма которых (252) делится на 4, а произведение (15552) делится на 2592. Ответ: 1.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
'''
with open('files/13/27-134a.txt') as f:
    n = int(f.readline())
    data = [int(i) for i in f]
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (data[i] + data[j]) % 7 == 0 and (data[i] * data[j]) % 2592 == 0:
                count += 1
print(count)

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac


print(primfacs(2592))

with open('files/13/27-134b.txt') as f:
    n = int(f.readline())
    pairs = [[[0]*(4+1) for d2 in range(5+1)] for _ in range(7)]
    count = 0
    for i in range(n):
        x = int(f.readline())
        r = x % 7
        r2 = 0 if r == 0 else 7-r
        d2 = 0
        while x % 2 ** (d2+1) == 0 and d2 < 5:
            d2 += 1
        d3 = 0
        while x % 3 ** (d3+1) == 0 and d3 < 4:
            d3 += 1
        count += sum(sum(pairs[r2][i2][4-d3:4+1]) for i2 in range(5-d2,5+1))
        pairs[r][d2][d3] += 1
print(count)


