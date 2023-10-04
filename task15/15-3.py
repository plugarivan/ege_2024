'''
Укажите наибольшее целое значение А, при котором выражение

(3y + 2x ≠ 130) ∨ (3x > A) ∨ (2y > A)
истинно для любых целых положительных значений x и y.


'''
def f(x, y):
    return ((3 * y + 2 * x) != 130) or (3 * x > a) or (2 * y > a)


for a in range(1000, 0, -1):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
