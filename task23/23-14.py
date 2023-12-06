'''Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 3
3. Умножить на 2
Программа для исполнителя Калькулятор – это последовательность команд. Сколько существует программ, для которых при исходном числе 3 результатом является число 20, и при этом траектория вычислений содержит числа 9 и 12?
'''
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)


print(f(3, 9) * f(9, 12) * f(12, 20))