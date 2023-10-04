'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наибольшего натурального числа A формула

¬ДЕЛ(x, A) → (¬ДЕЛ(x, 24) ∧ ¬ДЕЛ(x, 36))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

'''
def f(x):
    return (x % a != 0) <= ((x % 24 != 0) and (x % 36 != 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break