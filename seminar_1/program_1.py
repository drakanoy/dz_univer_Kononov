#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy  # импорт библиотек
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # начало программы
    arguments = numpy.arange(0, 200, 0.1)  # список большого количества точек)
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a / 20.0) for a in arguments]
    )  # строим по точкам функцию
    mpp.show()  # выводим картинку
