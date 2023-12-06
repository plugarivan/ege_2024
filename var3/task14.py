alph = '0123456789abcdefghijklmno'

for x in alph:
    f = int(f'1{x}2{x}3{x}4{x}5', 25) + int(f'2{x}024', 25) + int(f'1{x}099', 25)
    if f % 24 == 0:
        print(f // 24)