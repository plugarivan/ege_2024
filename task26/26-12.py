'''
На парковке есть L мест для легковых автомобилей и M мест для микроавтобусов. Приезжающий на парковку автомобиль занимает любое подходящее свободное место, при этом легковой автомобиль может встать на свободное место, предназначенное для микроавтобуса, но микроавтобус не может занять место, предназначенное для легкового автомобиля. Если подходящего свободного места нет, автомобиль уезжает. Гарантируется, что никакие два автомобиля не приезжают одновременно. Если время прибытия автомобиля совпадает со временем окончания стоянки другого автомобиля, вновь прибывший автомобиль может занять
освободившееся место, если оно подходит ему по типу.
Определите количество микроавтобусов, которые смогут припарковаться, и общее количество автомобилей (как легковых, так и микроавтобусов), которые уедут из-за отсутствия мест.
Входные данные представлены в файле 26-119.txt следующим образом. Первая строка входного файла содержит три целых числа: N – общее количество автомобилей, приехавших на парковку в течение суток; L – количество мест для легковых автомобилей и M – количество мест для микроавтобусов. Каждая из следующих N строк описывает один автомобиль и содержит два целых числа и букву. Первое число означает время в минутах с начала суток, когда автомобиль прибыл на парковку, второе – необходимую длительность стоянки в минутах. Буква означает тип автомобиля: A – легковой, B – микроавтобус.
В ответе запишите два целых числа: сначала количество микроавтобусов, которые смогут припарковаться, затем – общее количество автомобилей (как легковых, так и микроавтобусов), которые уедут из-за отсутствия мест.
'''
with open('files/26-119.txt') as f:
    n, l, m = map(int, f.readline().split())
    data = []
    for i in range(n):
        start, time, type = f.readline().split()
        data.append((int(start), int(start) + int(time), type))
    data.sort()
    busy = [0] * (l + m)
    countB = count = 0
    for x in data:
        place0 = 0 if x[2] == 'A' else l#потому что легковой может встать куда угодно, а автобус только в автобусное
        for place in range(place0, l + m):
            if x[0] >= busy[place]:
                busy[place] = x[1]
                countB += (x[2] == 'B')
                break
        else:
            count += 1
print(countB, count)