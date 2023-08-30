#Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

#funcs — список произвольных функций
#arg — произвольный объект

#Функция get_the_fastest_func() должна возвращать функцию из списка funcs,
#которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.

import time

def get_the_fastest_func(funcs, arg):
    result = []
    for c in funcs:
        start = time.monotonic()
        c(arg)
        end = time.monotonic()
        result.append(end - start)
    min_res = min(result)
    x = result.index(min_res)
    return funcs[x]