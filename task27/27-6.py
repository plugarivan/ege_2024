'''
В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны. Из этой последовательности нужно выбрать четыре числа, чтобы их сумма делилась на 4 и была наибольшей. Какую наибольшую сумму можно при этом получить?
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 108.
Пример входного файла:
6
6
4
13
11
10
8
Для указанных данных можно выбрать четвёрки 6, 4, 10, 8 (сумма 28), 6, 13, 11, 10 (сумма 40) и 4, 13, 11, 8 (сумма 36). Наибольшая из сумм – 40.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
'''
with open('files/6/27-54a.txt') as f:
    n = int(f.readline())
    data = [int(i) for i in f]
    maxim = 0
    for a in range(n - 3):
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                for d in range(c + 1, n):
                    if sum([data[a], data[b], data[c], data[d]]) % 4 == 0:
                        maxim = max(maxim, sum([data[a], data[b], data[c], data[d]]))
print(maxim)

with open('files/6/27-54b.txt') as f:
    n = int(f.readline())
    data = [int(i) for i in f]
    maxim = 0
    maxim1, maxim2, maxim3 = [0] * 4, [0] * 4, [0] * 4 #три списка для хранения наибольших сумм, количество элементов
    #в списке по количеству остатков от деления на 4
    # maxim1 - текущее наибольшее, в максим2 - сумма двух, в максим3 - сумма трех и в максим - сумма четырых
    for i in data:
        ostat = i % 4 #находим остаток от деления на 4 текущего числа
        maxim = max(maxim, i + maxim3[(4 - ostat) % 4])#сумма текущего элемента с максимальным числом
        # из 3 списка, у которых сумма остатка будет кратна 4 (к примеру, если у текущего остаток 3, то мы берем в пару к нему
        #тот у которого остаток 1 -> в сумме 4
        for d in range(4): #перебираем все остатки от 0 до 4 и заполняем списки самыми большими суммами, то есть в списке
            #maxim1 - текущее наибольшее, в максим2 - сумма двух, в максим3 - сумма трех и в максим - сумма четырых
            ostat0 = (d + ostat) % 4
            maxim3[ostat0] = max(maxim3[ostat0], maxim2[d] + i)
            maxim2[ostat0] = max(maxim2[ostat0], maxim1[d] + i)
        maxim1[ostat] = max(maxim1[ostat], i)
print(maxim)