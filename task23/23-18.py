'''Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Прибавить 3
Программа для исполнителя Калькулятор – это последовательность команд. Сколько существует программ, состоящих из 7 команд, для которых при исходном числе 3 результатом является число 22?
'''
def f(x, k):
    if x == 22 and k == 7:
        return 1
    elif x > 22:
        return 0
    return f(x + 1, k + 1) + f(x + 2, k + 1) + f(x + 3, k + 1)


print(f(3, 0))
