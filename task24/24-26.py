'''
(В. Шубинкин) Текстовый файл 24-268.txt состоит не более чем из 10**6 символов и содержит только заглавные буквы латинского алфавита и цифры. В файле записаны числа в девятнадцатеричной системе счисления, окружённые символами, не являющимися цифрами в этой системе счисления или началом/концом файла. Лидирующие нули в записи чисел не допускаются. Определите самое большое чётное число в этом файле. Например, в последовательности символов FF2FTZBBC8R420Y0CCCE содержится 3 числа в девятнадцатеричной системе счисления: FF2F, BBC8 и 420. Самое большое чётное число – BBC8. Число CCCE не учитывается, так как перед ним стоит ноль.
Алфавит девятнадцатеричной системы счисления: 0123456789ABCDEFGHI.
'''
s = open('files/24-268.txt').readline()
for letter in 'QWRTYUOPLKJSZXVNM':
    s = s.replace(letter, '*')
numbers = sorted(s.split('*'), key=len, reverse=True)
for num in numbers:
    if num[0] != '0' and int(num, 19) % 2 == 0:
        print(num)
        break
