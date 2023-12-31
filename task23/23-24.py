'''Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Прибавь 2
3. Умножь на 2
Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья – умножает на 2. Программа для исполнителя – это последовательность команд. Сколько существует программ, которые преобразуют исходное число 1 в число 12 и при этом не содержат двух команд «Прибавить 2» подряд?
'''
def f(x, y, command):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        if command == 0:
            return f(x + 1, y, 0) + f(x + 2, y, 1) + f(x * 2, y, 0)
        else:
            return f(x + 1, y, 0) + f(x * 2, y, 0)


print(f(1, 12, 0))
