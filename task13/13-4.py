'''Для узла с IP-адресом 124.128.112.142 адрес сети равен 124.128.64.0. Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.'''
from ipaddress import *

for m in range(33):
    net = ip_network(f'124.128.112.142/{m}', 0)
    if '124.128.64.0' in str(net):
        print(str(net.netmask)[8:11])