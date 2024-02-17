'''
Найдите все натуральные числа, принадлежащие отрезку [55 000 000; 60 000 000], у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым). В ответе перечислите найденные числа, справа от каждого числа запишите его наибольший нечётный делитель.
'''
#2 ** n * p ** 4 - у этого числа ровно 5 нечетных делителей
def simple(x):
    return all(x % d != 0 for d in range(2, round(x ** 0.5) + 1))


for n in range(55000000, 60000001):
    x = n
# убираем из разложения числа x на простые множители все двойки
    while x % 2 == 0:
        x //= 2
# находим корень четвёртой степени из того, что осталось
    sqrt4 = round(x ** 0.25)
# проверяем, является ли x четвёртой степенью простого числа
    if simple(sqrt4) and sqrt4 ** 4 == x:
        print(n, x)