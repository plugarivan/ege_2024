'''
Элементами множеств А, P и Q являются натуральные числа, причём P = { 1, 2, 4, 8 } и Q = { 1, 2, 3, 4, 5, 6 }. Известно, что выражение

¬(x ∈ A) → ¬((x ∈ P) ∨ (x ∈ Q))
истинно (т. е. принимает значение 1) при любом значении переменной х. Определите наименьшее возможное количество элементов множества A.

'''
p = {1, 2, 4, 8}
q = set(range(1, 7))
a = set()
for x in range(1, 1000):
    if not((x not in a) <= (not((x in p) or (x in q)))):
        a.add(x)
print(len(a))
