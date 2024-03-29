'''
(А.Н. Носкин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [190061; 190072], числа, имеющие ровно 4 различных НЕЧЁТНЫХ делителя. В ответе для каждого найденного числа запишите два его наибольших нечётных делителя в порядке убывания.
'''
for i in range(190061, 190073):
    divs = set()
    for d in range(1, int(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    d = [x for x in divs if x % 2]
    if len(d) == 4:
        print(sorted(d, reverse=True)[:2])
