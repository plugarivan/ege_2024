'''Определите наименьшее значение n, при котором сумма чисел, которые будут выведены при вызове F(n), будет больше 3200000. Запишите в ответе сначала найденное значение n, а затем через пробел – соответствующую сумму выведенных чисел.
Python
def F( n ):
  print(n*n)
  if n > 1:
    print(2*n+1)
    F(n-2)
    F(n//3)
'''
def f(n):
    global s
    s += (n * n)
    if n > 1:
        s += (2 * n + 1)
        f(n - 2)
        f(n // 3)


for n in range(10000):
    s = 0
    f(n)
    if s > 3200000:
        print(n, s)
        break

