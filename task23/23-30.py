'''Исполнитель преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 2
2. Умножь на 3
3. Умножь на 5
Первая команда увеличивает число на экране на 2, вторая умножает его на 3, третья – умножает на 5. Сколько существует различных программ, которые преобразуют исходное число 2 в число 200 и содержат не более трёх команд умножения?
'''
def f(x, y, k):
    if x > y:
        return 0
    if x == y:
        return 1
    if k < 3:
        return f(x + 2, y, k) + f(x * 3, y, k + 1) + f(x * 5, y, k + 1)
    else:
        return f(x + 2, y, k)


print(f(2, 200, 0))