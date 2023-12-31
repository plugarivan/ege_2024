'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, при n ≤ 3
при n > 3:
  F(n) = F(n–1) + 2*F(n/2), при чётном n;
  F(n) = F(n–1) + F(n-3), при нечётном n;
Определите количество натуральных значений n, при которых F(n) меньше, чем 108.
'''
f = [0] * 10 ** 5
for i in range(len(f)):
    if i <= 3:
        f[i] = i
    else:
        if i % 2 == 0:
            f[i] = f[i - 1] + 2 * f[i // 2]
        else:
            f[i] = f[i - 1] + f[i - 3]
print(len([n for n in range(1, len(f)) if f[n] < 10 ** 8]))
