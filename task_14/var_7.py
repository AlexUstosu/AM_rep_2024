#126)	(Е.А. Мирончик) Некоторое число X из десятичной системы счисления перевели
# в системы счисления с основаниями 16 и 8. Часть символов при записи утеряна.
# Позиции утерянных символов обозначены знаком *:
#X= 1*016 = 56*8
#Определите число X.


# alph = "0123456789ABCDEF"
# res = 0
#
# for i in alph:
#     n_16 = f'1{i}0'
#     n_8 = oct(int(n_16,16))[2:]
#     if len(n_8) == 3 and n_8[0] == '5'and n_8[1] == '6':
#         res = int(n_16,16)
#
# print(res)


#135
count = 0
alph = "0123456789ABCDEF"

for i in alph:
    n_16 = f'{i}A'
    n_8 = oct(int(n_16,16))[2:]
    if len(n_8) == 3:
        count += 1
print(count)