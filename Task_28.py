# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*

# 2 2   4

a = int(input("Введите число A (целое неотрицательное): "))
b = int(input("Введите число В (целое неотрицательно число: "))


def RecurSum(a, b):
    if a == 0:
        return b
    else:
        return RecurSum(a - 1, b + 1)


print(RecurSum(a, b))
