'''
На производстве штучных изделий N деталей должны быть отшлифованы и окрашены. Для каждой детали известно время её шлифовки и время окрашивания. Детали пронумерованы начиная с единицы. Параллельная обработка деталей не предусмотрена. На ленте транспортёра имеется N мест для каждой из N деталей. На ленте транспортёра детали располагают по следующему алгоритму:
– все 2N чисел, обозначающих время окрашивания и шлифовки для N деталей, упорядочивают по возрастанию;
– если минимальное число в этом упорядоченном списке – это время шлифовки конкретной детали, то деталь размещают на ленте транспортёра на первое свободное место от её начала;
– если минимальное число – это время окрашивания, то деталь размещают на первое свободное место от конца ленты транспортёра
– если число обозначает время окрашивания или шлифовки уже рассмотренной детали, то его не принимают во внимание.
Этот алгоритм применяется последовательно для размещения всех N деталей. Определите номер последней детали, для которой будет определено её место на ленте транспортёра, и количество деталей, которые будут отшлифованы до неё.
Входные данные представлены в файле 26-129.txt следующим образом. Первая строка входного файла содержит натуральное число N (1 ≤ N ≤ 1000) – количество деталей. Следующие N строк содержат пары чисел, обозначающих соответственно время шлифовки и время окрашивания конкретной детали (все числа натуральные, различные).
Запишите в ответе два натуральных числа: сначала номер последней детали, для которой будет определено её место на ленте транспортёра, затем количество деталей, которые будут отшлифованы до неё.
'''
with open('files/26-129.txt') as F:
    n = int(F.readline())
    data = []
    for i in range(n):
        t1, t2 = map(int, F.readline().split())
        if t1 < t2:
            data.append((t1, 1, i + 1))
        else:
            data.append((t2, 2, i + 1))
data.sort()
konveer = [0] * n
n1 = 0  # начало ленты
n2 = n - 1  # конец ленты
for t, op, no in data:  # перебираем список, t - время обработки, op - флаг 1 или 2, no - номер детали
    if op == 1:
        konveer[n1] = no
        n1 += 1
    else:
        konveer[n2] = no
        n2 -= 1
print(data[-1][2],
      n1 if data[-1][1] == 2 else n1 - 1)



