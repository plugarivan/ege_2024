'''
Среди целых чисел, принадлежащих числовому отрезку [351627;428763], найдите числа, которые представляют собой произведение двух различных простых делителей. Запишите в ответе количество таких чисел и их среднее арифметическое. Для среднего арифметического запишите только целую часть числа.
'''
def simple(x):
    return all(x % d != 0 for d in range(2, round(x ** 0.5) + 1))


count, summa = 0, 0
for i in range(351627, 428764):
    for d in range(2, round(i ** 0.5)):#различные значит корень не берем
        if d * (i // d) == i and simple(d) and simple(i // d):
            count += 1
            summa += i
print(count, summa // count)