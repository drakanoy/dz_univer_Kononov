#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typeguard import typechecked

ITERATIONS = 100


@typechecked
def my_arcsin(x: float) -> float:  # считаем арксинус. эта функция подходит для -1<=x<=1
    """
    Вычисление Арксинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    эта функция подходит для -1<=x<=1
    """
    multiplier = 1
    partial_sum = x
    new_x = x
    for n in range(3, ITERATIONS, 2):
        multiplier *= (n - 2) / (n - 1)
        new_x = x ** n
        partial_sum += new_x / n * multiplier
    return partial_sum


try:
    print(my_arcsin(0.5))
    print('float можно')
except:
    print('float нельзя')

try:
    print(my_arcsin(0))
    print('int можно')
except:
    print('int нельзя')

try:
    print(my_arcsin(1 + 1j))
    print('complex можно')
except:
    print('complex нельзя')

try:
    print(my_arcsin('1'))
    print('str можно')
except:
    print('str нельзя')

try:
    print(my_arcsin([0.5]))
    print('list можно')
except:
    print('list нельзя')
