'''
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 2?5432*1, делящиеся на 1017 без остатка и содержащие хотя бы одну цифру 9. В ответе запишите все найденные числа в порядке возрастания, справа от каждого числа – результат его деления на 1017.
'''
from fnmatch import fnmatch

for n in range(0, 10 ** 10 + 1, 1017):
    if fnmatch(str(n), '2?5432*1') and '9' in str(n):
        print(n, n // 1017)
