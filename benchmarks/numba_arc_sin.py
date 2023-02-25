#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numba import float64
from numba.experimental import jitclass
from numba import jit


@jitclass([
    ('x', float64),
    ('partial_sum', float64), ('new_x', float64), ('multiplier', float64), ('TERATIONS', float64)
])
class My_arcsin():
    def __init__(self):
        self.x = 3.1415926 / 4

    def my_arcsin(self) -> float64:  # считаем арксинус numba
        ITERATIONS = 100
        multiplier = 1
        partial_sum = self.x / 3.1415926 / 2
        new_x = self.x / 3.1415926 / 2
        for n in range(3, ITERATIONS, 2):
            multiplier *= (n - 2) / (n - 1)
            new_x = self.x ** n
            partial_sum += new_x / n * multiplier
        self.x = partial_sum
        return partial_sum
