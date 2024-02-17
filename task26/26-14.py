'''
Для анализа нагрузки сервера для каждого запроса в журнал записываются время начала и время завершения его обработки (в миллисекундах от момента начала исследований). Если начальное время равно 0, запрос начал обрабатываться до начала исследований, если конечное время равно 0, то обработка запроса закончилась после окончания исследований. Необходимо определить наибольшее количество запросов, которые сервер обрабатывал одновременно в течение суток, начиная с момента K, и суммарное время, в течение которого обрабатывалось это максимальное количество запросов.
Входные данные представлены в файле 26-66.txt следующим образом. Первая строка входного файла содержит количество записей N и время K. Каждая из следующих N строк содержит два целых числа: время начала и время завершения обработки одного запроса (в миллисекундах).
Запишите в ответе два числа: наибольшее количество запросов, которые сервер обрабатывал одновременно в течение указанных суток, и суммарное время, в течение которого обрабатывалось это максимальное количество запросов.
'''
with open('files//26-66.txt') as f:
    n, start = map(int, f.readline().split())
    end = start + 24 * 3600 * 1000
    miliseconds = {i: 0 for i in range(start, end + 1)} #создаем словарь где ключи это милисекунды в заданном промежутке, а значения пока 0
    files = [list(map(int, i.split())) for i in f]#в список помещаем списки (начало и конец процесса)
    for x in files:
        if (x[0] < end or x[0] == 0) and (x[1] > start or x[1] == 0): #если процесс входит в наш промежуток
            if (x[0] == 0 or x[0] < start): x[0] = start#если входит то время начала заменяем с 0 на время начало
            if (x[1] == 0 or x[1] > end): x[1] = end#если входит то время конца заменяем с 0 на время окончания
            miliseconds[x[0]] += 1 #в эту милисекунды счетчик начавшихся процессов
            miliseconds[x[1]] -= 1#в эту милисекунды счетчик процессов, которые закончились
k = kmax = count = 0
for i in miliseconds.items():
    k += i[1]
    if k > kmax:
        kmax = k
        count = 0
    if k == kmax:
        count += 1
print(kmax, count)