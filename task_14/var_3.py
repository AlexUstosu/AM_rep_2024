# for i in range(2,100):
#     x = 67
#     x_N = ''
#     while x > 0:
#         x_N += str(x % i)
#         x //= i
#     x_N = x_N[::-1]
#     if x_N[-1] == '1' and len(x_N) == 4:
#         print(x_N)
#         break

#Укажите через запятую в порядке возрастания все десятичные числа,
# не превосходящие 25, запись которых в системе счисления с основанием
# четыре оканчивается на 11?

# for i in range(1,26):
#     x = i
#     x_4 = ''
#     while x > 0:
#         x_4 += str(x % 4)
#         x //= 4
#     x_4 = x_4[::-1]
#     if x_4[-2:] == '11':
#         print(f'{i},')



# for number in '0', '1':
#     print(f'{int(number + '11',4)}, ')

#Укажите через запятую в порядке возрастания все
# основания систем счисления, в которых запись числа 23 оканчивается на 2.

#k * N + 2 = 23



