'''
(К. Багдасарян) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети. Сеть задана IP-адресом 211.48.136.64 и маской сети 255.255.255.224. Сколько в этой сети IP-адресов, которые в двоичной записи IP-адреса оканчиваются двумя единицами?
В ответе укажите только число.
'''
from ipaddress import *

k = 0
net = ip_network(f'211.48.136.64/255.255.255.224', 0)
for ip in net:
    ip_bin = bin(int(ip))[2:]
    if ip_bin[-2:] == '11':
        k += 1
print(k)
