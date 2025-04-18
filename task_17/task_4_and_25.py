#371)	В файле 17-370.txt содержится последовательность
# целых чисел, по модулю не превышающих 20000.
# Определите количество пар элементов последовательности,
# в которых
#– только одно число четырёхзначное;
#– сумма квадратов элементов пары делится нацело на максимальное
# трёхзначное число в последовательности, сумма цифр которого оканчивается
# на 3.
# В ответе запишите сначала количество найденных пар,
# затем максимальную из сумм квадратов элементов таких пар.
# Под парой элементов подразумеваются два соседних элемента
# последовательности.

# new_list = []
# list_3_nubers = []
# max_list_3_numbers = []
# result = []
# with open('17-370.txt', 'r') as file:
#     for line in file:
#         new_list.append(int(line))
# print (new_list)
#
# true_3_numbers = 0
# for i in new_list:
#     if len(str(abs(i))) == 3:
#          list_3_nubers.append(i)
#
# print (f'Трехзначные: \n{list_3_nubers}')
#
# for x in list_3_nubers:
#     summa_chisel = (x % 10) + (x % 100 // 10) + (x // 100)
#     if summa_chisel % 10 == 3:
#         max_list_3_numbers.append(x)
#
# print (f'Трехзначные с отобранной суммой: \n{max_list_3_numbers}')
# max_3 = max(max_list_3_numbers)
# print (f'Максимальное: \n{max_3}')
#
# for i in range(len(new_list) - 1):
#     x_1 = new_list[i]
#     x_2 = new_list[i + 1]
#
#
#     pow_sum = x_1 ** 2 + x_2 ** 2
#     if (1000 <= abs(x_1) <= 9999) and not(1000 <= abs(x_2) <= 9999)\
#             or not(1000 <= abs(x_1) <= 9999) and (1000 <= abs(x_2) <= 9999):
#         if pow_sum % max_3 == 0:
#             result.append(pow_sum)
#             print("Pair:", x_1, "\t", x_2)
#
# print (f'Количество пар: \n{len(result)}')
# print (f'Результирующий массив: \n{result}')
# print (f'Максимальное: \n{max(result)}')



# 25 task
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [174457; 174505], числа,
# имеющие ровно два различных натуральных делителя, не считая единицы и самого числа.
# Для каждого найденного числа запишите эти два делителя в таблицу на экране
# с новой строки в порядке возрастания произведения этих двух делителей.
# Делители в строке таблицы также должны следовать в порядке возрастания

# 1. целые числа
# 2. шестизначные, положительные
# 3. натуральные делители
# 4. различные
# 5. НЕ 1 НЕ число
# 6. Эти числа по списку
# 7. два делителя на экран в виде произведения
# 8.
# 4 5
# 2 3


#
#
# import math
# dives = []
# for number in range(174457, 174506):
#     end = int(math.sqrt(number))
#
#     for delitel in range(2, end + 1):
#         if number % delitel == 0:
#             if delitel == number // delitel:
#                 dives = dives + delitel
#             else:
#                 dives = dives + [delitel, number // delitel]
#             if len(dives) > 2:
#                 break
#     if len(dives) == 2:
#         print(dives)





#337)	(И. Кушнир) В файле 17-336.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Обозначим через M максимальный элемент последовательности, кратный 37.
# Определите количество пар последовательности, в которых хотя бы одно число делится на M,
# а сумма элементов пары при делении на M дает в остатке число, большее 30.
# Гарантируется, что такая пара в последовательности есть.
# В ответе запишите количество найденных пар и минимальную сумму элементов среди таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# new_list = []
# with open('17-316.txt', 'r') as file:
#     for line in file:
#         new_list.append(int(line))
# print (new_list)
#
#
# max_element = []
# M = 0
# for i in new_list:
#     if i % 37 == 0:
#         max_element.append(i)
# M = max(max_element)
# print(M)
#
# result_list = []
# k = 0
# for i in range(len(new_list) - 1):
#     x_1 = new_list[i]
#     x_2 = new_list[i+1]
#     if (x_1 % M == 0) or (x_2 % M == 0):
#         if (x_1 + x_2) % M > 30:
#             result_list.append(x_1 + x_2)
#             k += 1
# print (f"Количество пар: {k}")
# print (f"минимальную сумму элементов: {min(result_list)}")




#344)	(Е. Джобс) В файле 17-344.txt содержится последовательность целых чисел.
# Элементы последовательности – натуральные числа, не превосходящие 100000.
# Определите количество пар последовательности, в которых сумма чисел четна,
# а разница между числами кратна минимальному числу, кратному 103.
# Гарантируется, что элемент, кратный 103, в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную
# из сумм элементов таких пар. В данной задаче под парой подразумевается
# два идущих подряд элемента последовательности.


# new_list = []
# with open('17-344.txt', 'r') as file:
#     for line in file:
#         new_list.append(int(line))
# print (new_list)
#
#
# min_element = []
# M = 0
# for i in new_list:
#     if i % 103 == 0:
#         min_element.append(i)
# M = min(min_element)
# print(M)
#
# result_list = []
# for i in range(len(new_list) - 1):
#     x_1 = new_list[i]
#     x_2 = new_list[i+1]
#     summa = x_1 + x_2
#     division = x_1 - x_2
#     if summa % 2 == 0 and division % M == 0:
#             result_list.append(summa)
#     summa = 0
#     division = 0
#
#
# print (f"Количество пар: {len(result_list)}")
# print (f"Max сумму элементов: {max(result_list)}")




#353)	(Е. Джобс) В файле 17-353.txt содержится последовательность натуральных чисел,
# не превышающих 10000. Симметричной парой называется такая пара чисел в заданной
# последовательности, элементы которой расположены на равном расстоянии от концов
# последовательности. Например, в последовательности 1 2 3 4 3 5 1 симметричными
# парами назовем пары (1, 1), (2, 5), (3, 3). Число 4 не образует пару, так как оно
# находится на равном удалении от краев, следовательно, это одно число, а не два.
# Найдите количество симметричных пар таких, что среднее арифметическое максимального
# и минимального значений последовательности строго меньше значения одного элемента пары
# и строго больше значения второго элемента пары.
# В качестве ответа запишите количество найденных пар и максимальную сумму
# элементов среди найденных пар.

# data = [int(x) for x in open('17-353.txt')]
# new_list = []
# with open('17-353.txt', 'r') as file:
#     for line in file:
#         new_list.append(int(line))
# print (new_list)
#
# average = (max(new_list) + min(new_list)) / 2
#
# result_list = []
# for i in range(len(new_list) // 2 + 1):
#     if i == len(new_list) // 2 and len(new_list) % 2 != 0:
#         break
#     x_1 = new_list[i]
#     x_2 = new_list[len(new_list) - 1 - i]
#
#     if (x_1 < average and x_2 > average) or (x_2 < average and x_1 > average) :
#             result_list.append(x_1 + x_2)
#
# print (f"Количество пар: {len(result_list)}")
# print (f"Max сумму элементов: {max(result_list)}")


#2120 14972


#93)	(П. Волгин)  Рассматривается множество четных целых чисел,
# принадлежащих числовому отрезку [100; 1000], которые удовлетворяют следующим условиям:
#а) Число в шестнадцатеричной записи оканчивается цифрой «0»;
#б) Число не делится на 3.
#Найдите сумму таких чисел и их количество.
# В ответе запишите сначала сумму, а потом количество.


list = [ i for i in range (100, 1001)]

new_list = []
for i in list:
    hex_i = hex(i)[2:]
    if hex_i[-1:] == '0' and i % 3 != 0:
        new_list.append (i)
print (sum(new_list))
print (len(new_list))




