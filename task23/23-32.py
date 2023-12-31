'''*(М. Шагитов) Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены коды:

A. Прибавь 3
B. Умножь на 4
C. Умножь на 5
Выполняя первую из них, исполнитель увеличивает число на экране на 3, выполняя вторую – умножает на 4, выполняя третью – умножает на 5. Программой для исполнителя называется последовательность команд. Сколько существует программ, для которых при исходном числе 1 результатом будет являться число 725, при этом траектория вычисления содержит числа 16 и 152, и на промежутке траектории между этими числами последовательность команд является палиндромом. Траектория вычисления программы – это последовательности результатов выполнения всех команд. Например, для программы CAB при исходном числе 4 траектория будет состоять из чисел 20, 23, 92.
'''
def f(x, y, pal, s):
    if x > y: return 0
    if x == y: return s == s[::-1] if pal else 1
    return f(x + 3, y, pal, s + 'A') + f(x * 4, y, pal,  s + 'B') + f(x * 5, y, pal, s + 'C')


print(f(1, 16, False, '') * f(16, 152, True, '') * f(152, 725, False, ''))