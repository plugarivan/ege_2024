'''
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Найдите все числа, меньшие 10**8, соответствующие маске 1*2??76 и делящиеся без остатка на 1923. В качестве ответа приведите все найденные числа в порядке возрастания, справа от каждого числа выведите результат его деления на 1923.
'''
from fnmatch import fnmatch

for n in range(0, 10 ** 8 + 1, 1923):
    if fnmatch(str(n), '1*2??76'):
        print(n, n // 1923)
