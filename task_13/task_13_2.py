# https://kpolyakov.spb.ru/school/ege.htm
# http
# ftp
#
# IP - 32 бит
# 8бит.8бит.8бит.8бит
# 00000000.мин
# 11111111.макс
# 0-255.0-255.0-255.0-255
# сеть и подсеть
# 255.255.255.0
# 11111111.11111111.11111111.00000000
#
# 192.168.3.1
# 11000000.10101000.00000011.00000001
#
# 192.168.3.23
# 11000000.10101000.00000011.00010111
from openpyxl.packaging.manifest import mimetypes

from main import minimum

#Р-13. Для узла с IP-адресом 15.51.208.15 адрес сети равен 15.51.192.0.
# Найдите наименьшее возможное количество единиц в двоичной записи маски подсети.

# from ipaddress import *
# for i in range(32):
#   net = ip_network("15.51.208.15/" + str(i),0)
#   print(net)
#   param = str(net).split('/')
#   print(param)
#   if param[0] == "15.51.192.0":
#     param_10 = int(net.netmask)
#     print(param_10)
#     param_2 = bin(param_10)[2:]
#     print(param_2)
#     print(param_2.count('1'))
#     break


# Р-12 (Демо-2024). В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в
# результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240. Сколько в этой сети IP-адресов,
# для которых сумма единиц в двоичной записи IP-адреса чётна? В ответе укажите только число.

# 240 = 11110000
# 2^4 = 16
# 8


# from ipaddress import *
#
# net = ip_network("192.168.32.160/255.255.255.240")
# print(net)
# count = 0
# for i in net.hosts():
#   if bin(int(i)).count('1') % 2 == 0:
#     count += 1
# print(count + 2)


# Р-11. Два узла, находящиеся в разных подсетях, имеют IP-адреса 192.168.106.35 и 192.168.106.117.
# В масках обеих подсетей одинаковое количество единиц. Укажите наименьшее и наибольшее возможное количество единиц
# в масках этих подсетей. Учтите, что два адреса в любой подсети зарезервированы: адрес всей подсети и широковещательный адрес.

# 255.255.255.? - для наибольшего варианта
# 255.255.?.0  - для наименьшего варианта
#
# 10101
# 10001
#
# & | <<
#
# 4 and 5
# 4 && 5 = true / false
#
# 4 & 5 = 4
# 0100
# 4 << 1
# 1000 = 8
# 4 >> 2 = 1
# 0001
# 0101

# mask = [0, 128, 192, 224, 240, 248, 252, 254, 255]
# for i in mask:
#   if i & 35 != i & 117 and i != 255:    #max
#     print(i, 8 * 3 + bin(i).count('1'))
#
# for i in mask:
#   if i & 106 != i & 106:    #min
#     print(i, 8 * 2 + bin(i).count('1'))
#
# от 26 до 29


# Р-10. Два узла, находящиеся в одной подсети, имеют IP-адреса 195.157.132.140 и 195.157.132.176.
# Укажите наименьшее возможное количество адресов в этой сети.

# 140 = 10 001100
# 176 = 10 110000
#


# from ipaddress import *
#
# min_ = 2 ** 32
# for i in range(32):
#   net1 = ip_network("195.157.132.140/" + str(i),0)
#   net2 = ip_network("192.168.32.160/" + str(i),0)
#
#   str1 = str(net1).split('/')
#   str2 = str(net2).split('/')
#
#   if str1[0] == str2[0]:
#     count = net1.num_addresses
#     if count < min_:
#       min_ = count
# print(min_)






# Р-09. Для узла с IP-адресом 71.192.0.12 адрес сети равен 71.192.0.0. Для скольких различных значений маски это возможно?

#сделать

# Р-08. Два узла, находящиеся в одной сети, имеют IP-адреса 118.222.130.140 и 118.222.201.140.
# Укажите наибольшее возможное значение третьего слева байта маски сети. Ответ запишите в виде десятичного числа.

#сделать

# Р-07. В терминологии сетей TCP/IP маска сети – это двоичное число, меньшее 232;
# в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места нули. Маска определяет, какая часть IP-адреса
# узла сети относится к адресу сети, а какая – к адресу самого узла в этой сети. Обычно маска записывается по тем же правилам,
# что и IP-адрес – в виде четырёх байт, причём каждый байт записывается в виде десятичного числа.
# Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и маске.
# Например, если IP-адрес узла равен 221.32.255.131, а маска равна 255.255.240.0, то адрес сети равен 221.32. 240.0.
# Для узла с IP-адресом 124.128.112.142 адрес сети равен 124.128.64.0. Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.

# 221.32.255.131
# 255.255.240.0
# 221.32.240.0
#
# 255.255..0
#
# 112 = 01 11 0000
# 64 =  01 00 0000



from ipaddress import *

for i in range(32):
  net1 = ip_network("124.128.112.142/" + str(i),0)
  str1 = str(net1).split('/')

  if str1[0] == '124.128.64.0':
    print(net1.netmask)

# Р-05. В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса
# узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения
# поразрядной конъюнкции к заданному адресу узла и его маске. По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 10.8.248.131		Маска: 255.255.224.0

# Р-02. Маской подсети называется 32-разрядное двоичное число, которое определяет, какая часть
# IP-адреса компьютера относится к адресу сети, а какая часть IP-адреса определяет номер (внутренний адрес)
# компьютера в подсети. В маске подсети старшие биты, отведенные в IP-адресе компьютера для адреса сети, имеют значение
# 1;младшие биты, отведенные в IP-адресе компьютера для номера (внутреннего адреса) компьютера в подсети, имеют значение 0.Например, маска подсети может иметь вид:
# 11111111 11111111 11100000 00000000 (255.255.224.0)
# Это значит, что 19 старших бит в IP-адресе содержит адрес сети, оставшиеся 13 младших бит содержат номер (внутренний адрес)
# компьютера в сети. Если маска подсети 255.255.255.240 и IP-адрес компьютера в сети 162.198.0.44, то номер компьютера в сети равен_____

# Р-01. Маской подсети называется 32-разрядное двоичное число, которое определяет, какая часть IP-адреса компьютера
# относится к адресу сети, а какая часть IP-адреса определяет номер (внутренний адрес) компьютера в подсети.
# В маске подсети старшие биты, отведенные в IP-адресе компьютера для адреса сети, имеют значение 1;младшие биты,
# отведенные в IP-адресе компьютера для номера (внутреннего адреса) компьютера в подсети, имеют значение 0.Например, маска подсети может иметь вид:
# 11111111 11111111 11100000 00000000 (255.255.224.0)
# Это значит, что 19 старших бит в IP-адресе содержит адрес сети, оставшиеся 13 младших бит содержат номер
# (внутренний адрес) компьютера в сети. Если маска подсети 255.255.240.0 и IP-адрес компьютера в сети 162.198.75.44, то номер компьютера в сети равен_____