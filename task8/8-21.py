'''
Определите количество семизначных чисел, записанных в девятеричной системе счисления, учитывая, что числа не могут заканчиваться на цифры 3, 4 и 7 и не должны содержать тройки соседних одинаковых цифр (например, 000).
'''
from itertools import product
def valid(s):
    if s[-1] in '347': return False
    for i in range(9):
        if (str(i)+str(i)+str(i)) in s:
            return False
    return True


k = 0
for w in product('012345678', repeat=7):
    numb = ''.join(w)
    if valid(numb) and numb[0] != '0':
        k += 1
print(k)