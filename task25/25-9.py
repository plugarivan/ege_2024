'''
Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу. Найдите все натуральные числа, принадлежащие отрезку [525784203; 728943762] и имеющие ровно три нетривиальных делителя. Для каждого найденного числа запишите в ответе два числа: само число и его наибольший нетривиальный делитель. Найденные числа расположите в порядке возрастания.
'''
#Три нетривиальных делителя имеют только(!) простые числа в четвертой степени
#В решение ищутся такие простые числа, чтобы p^4 = z, потому что тогда существует строго 3 нетривиальных делителя: p, p^2, p^3
def simple(x):
    return all(x % d != 0 for d in range(2, round(x ** 0.5) + 1))


for q4 in range(round(525784203 ** 0.25), round(728943762 ** 0.25) + 1):
    x = q4 ** 4
    if 525784203 <= x <= 728943762 and simple(q4):
        print(x, max(q4, q4 ** 2, q4 ** 3))


