'''По заданным IP-адресу узла сети и маске определите адрес сети:

  IP-адрес: 32.130.201.117
  Маска: 255.255.240.0
При записи ответа выберите из приведенных в таблице чисел 4 фрагмента четыре элемента IP-адреса и запишите в нужном порядке соответствующие им буквы без точек.
'''
from ipaddress import *
print(ip_network('32.130.201.117/255.255.240.0', 0))
