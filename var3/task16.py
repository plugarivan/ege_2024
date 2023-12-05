f = [1] * 2100
for n in range(len(f)):
    if n == 2: f[n] = 2
    if n > 2:
        f[n] = n * (n - 1) + f[n - 1] + f[n - 2]
print(f[2024] - f[2022] - 2 * f[2021] - f[2020])