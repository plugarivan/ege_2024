'''Определите, сколько символов * выведет эта процедура при вызове F(140):
Python
def F( n ):
  print('*')
  if n >= 1:
    print('*')
    F(n-1)
    F(n//2)
'''
def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n - 1)
        f(n // 2)


k = 0
f(140)
print(k)