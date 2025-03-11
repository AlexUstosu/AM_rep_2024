# from itertools import combinations, repeat
#
# combine = list(combinations('AN+', 2))
# print(combine)
#
#
# from itertools import permutations
#
# combine1 = list(permutations('AN+'))
# print(combine1)
#
#
# from itertools import product
#
# combine2 = product('AN+',repeat = 2)
# # for i in combine2:
# #     s_new = "".join(i)
# #     print(s_new)
#
# combine2 = list(map("".join, combine2))
# print(combine2)
from collections.abc import bytes_iterator
#Р-11 (демо-2021).  Игорь составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Игорь использует трёхбуквенные слова, в которых могут быть только буквы Ш, К, О, Л, А, причём буква
# К появляется ровно 1 раз. Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз
# или не встречаться совсем. Сколько различных кодовых слов может использовать Игорь?


# from itertools import product
#
# combine2 = [i for i in product('ШКОЛА',repeat = 3) if i.count('К') == 1]
# print(len(combine2))

# combine2 = product('ШКОЛА',repeat = 3)
# count1 = 0
# for i in combine2:
#     if i.count('К') == 1:
#         count1 += 1
# print(count1)


#Р-03. Все 4-буквенные слова, составленные из букв К, Л, Р, Т, записаны в алфавитном порядке и пронумерованы. Вот начало списка:
# 1. КККК
# 2. КККЛ
# 3. КККР
# 4. КККТ
# Запишите слово, которое стоит на 67-м месте от начала списка

from itertools import product
print(list(product('КЛРТ',repeat = 4))[66])



I = N * K
I - информационный объем
K - число бит на символ
N - количество символов

Q = 2^K

Q = M^N

# Р-12 (ЕГЭ-2024). На предприятии каждой изготовленной детали присваивают серийный номер, состоящий из 261 символов.
# Для его хранения отведено одинаковое и минимально возможное целое число байт. При этом используется посимвольное
# кодирование серийных номеров, все символы кодируются одинаковым и минимально возможным числом бит. Известно,
# что для хранения 252 500 серийных номеров отведено более 31 Мбайт памяти. Определите минимально возможную мощность
# алфавита, из которого составляются серийные номера. В ответе запишите только число.

I = 31 * 1024 * 1024 / 252500 =  128.7.... === 129
128 * 8 = 1024 bit

1024 / 261 = 4

#Р-11 (ЕГЭ-2024). На предприятии каждой изготовленной детали присваивается серийный номер,
# содержащий десятичные цифры и символы из 2030-символьного специального алфавита. В базе данных для
# хранения каждого серийного номера отведено одинаковое и минимально возможное целое число байт. При
# этом используется посимвольное кодирование, все символы кодируются одинаковым и минимально возможным
# числом бит. Известно, что для хранения 318 серийных номеров отведено более 67 Кбайт памяти. Определите
# минимально возможную длину серийного номера. В ответе запишите только целое число.

67 * 1024
215
215 * 8 = 1720
2040 = 2^11


#Р-10 (демо-2021). При регистрации в компьютерной системе каждому объекту сопоставляется
# идентификатор, состоящий из 15 символов и содержащий только символы из 8-символьного набора:
# А, В, C, D, Е, F, G, H. В базе данных для хранения сведений о каждом объекте отведено одинаковое и
# минимально возможное целое число байт. При этом используют посимвольное кодирование идентификаторов,
# все символы кодируют одинаковым и минимально возможным количеством бит. Кроме собственно идентификатора,
# для каждого объекта в системе хранятся дополнительные сведения, для чего отведено 24 байта на один объект.
# Определите объём памяти (в байтах), необходимый для хранения сведений о 20 объектах.
# В ответе запишите только целое число – количество байт.


8 символов = 3 бита
15 * 3 = 45 бит - 64 бит - 6 байт
id + доп инфа = (6 + 24) * 20 = 600


#Р-09. Информационная панель может отображать сообщения, состоящие из 10 цифр,
# причем каждая цифра может быть трёх цветов. Цифры и цвета могут повторяться.
# Контроллер панели выделяет под каждое сообщение одинаковое и минимальное возможное целое число байт.
# При этом используется посимвольное кодирование, все символы сообщения кодируются одинаковым минимально
# возможным количеством бит. Укажите объем памяти в байтах для хранения 100 сообщений.


#Р-08. При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 11 символов.
# Из соображений информационной безопасности каждый пароль должен содержать хотя бы 2 десятичных цифры, как прописные,
# так и строчные латинские буквы, а также не менее 2-х символов из 6-символьного набора: «&», «#», «$», «*», «!», «@».
# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством
# бит. Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения,
# для чего выделено целое число байт; это число одно и то же для всех пользователей. Для хранения сведений
# о 30 пользователях потребовалось 900 байт. Сколько байт выделено для хранения дополнительных сведений об
# одном пользователе? В ответе запишите только целое число – количество байт.

1. 30 байт на пользователя
2. пароль + доп инфа
3. 10 6 26 26 = 68  = 7 бит
4. 7 * 11 = 77 = 10 байт
