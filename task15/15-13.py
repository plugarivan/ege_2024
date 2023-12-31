'''
(А. Кабанов) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m» ; и пусть на числовой прямой дан отрезок B = [160; 180]. Для какого количества различных натуральных значений числа А формула

(x ∈ B) → (ДЕЛ(x, 35) → ДЕЛ(x, A))
тождественно истинна, то есть принимает значение 1 при любом натуральном значении переменной х?

'''
def f(x):
    return (x in range(160, 181)) <= ((x % 35 == 0) <= (x % a == 0))


k = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        k += 1
print(k)