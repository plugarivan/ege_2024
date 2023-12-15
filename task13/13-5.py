'''Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0. Чему равно наименьшее возможное значение третьего слева байта маски?'''
from ipaddress import *

for m in range(33):
    net = ip_network(f'111.81.208.27/{m}', 0)
    if '111.81.192.0' in str(net):
        print(str(net.netmask)[8:11])
        break
