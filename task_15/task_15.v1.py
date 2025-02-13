# Р-33.  (С.С. Поляков) Укажите наибольшее целое значение А, при котором выражение
# (y – x  5) ∨ (A < 2x3 + y) ∨ (A < y2 + 16)
#истинно для любых целых положительных значений x и y.
# def F(y,x, A):
#     return (y - x != 5) or (A < 2 * x ** 3 + y) or (A < y ** 2 + 16)
#
# for A in range(1, 1000):
#     flag = True
#     for y in range(1, 1000):
#         for x in range(1, 1000):
#             if not F(y,x,A):
#                 flag = False
#                 break
#     if flag:
#         print(A)


# Р-35  (демо-2021). Обозначим через ДЕЛ(n,m) утверждение «натуральное число n делится без
# остатка на натуральное число m». Для какого наибольшего натурального числа А формула
# ¬ДЕЛ(x,А)(ДЕЛ(x,6) ¬ДЕЛ(x,9))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
def Del(n, m):
    return n % m == 0

def F(x, A):
    return (not Del(x, A)) <= (Del(x, 6) <= (not Del(x,9)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not F(x,A):
                flag = False
                break
    if flag:
        print(A)