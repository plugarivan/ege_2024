
'''
(А.М. Кабанов) В текстовом файле k7a-5.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки, не содержащей символов C и F.
'''
s = open('files/k7a-5.txt').readline()
k = kmax = 0
for i in s:
    if i not in 'CF':
        k += 1
        kmax = max(k, kmax)
    else:
        k = 0
print(kmax)