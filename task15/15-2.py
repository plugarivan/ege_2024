'''
Укажите наименьшее целое значение А, при котором выражение

(– y + 2x < A) ∨ (x > 15) ∨ (y > 28)
истинно для любых целых положительных значений x и y.

'''
def f(x, y):
    return (-y + 2 * x < a) or (x > 15) or (y > 28)


for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break