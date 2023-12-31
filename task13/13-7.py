'''(М. Ишимов) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети. Для узла с IP-адресом 229.117.114.172 адрес сети равен 229.117.112.0. Каково наименьшее возможное количество единиц в двоичной записи маски?'''
from ipaddress import *

for m in range(33):
    net = ip_network(f'229.117.114.172/{m}', 0)
    if '229.117.112.0' in str(net):
        print(m)
        break
