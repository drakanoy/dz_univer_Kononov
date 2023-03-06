#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from semestor1.quaternion import Quaternion
from gauss import vector_gauss
from numpy import array, matmul

a11 = Quaternion(-1.98584, -5.31919, 5.68637, 0.09948)
a12 = Quaternion(-5.80444, 6.38001, 8.40159, -2.78770)
a21 = Quaternion(-1.75054, -2.26277, 6.73862, -9.10515)
a22 = Quaternion(-1.49604, 10.34792, -4.47970, 6.79651)
b1 = Quaternion(-6.72126, -4.23298, -9.45389, -1.67684)
b2 = Quaternion(5.02906, -6.03885, -10.79951, 1.12021)

a = array([
    [a11, a12],
    [a21, a22]
], dtype=Quaternion)
b = array([b1, b2], dtype=Quaternion)

s = vector_gauss(a, b)
print('в 1 примере кватернионы сгенерированны в random.org')
print(s)
print('проверка точности для 1 промера')
print(matmul(a, s) - b)
print('как видим точность моего гаусса для случайных кватернионов плохая')

a11 = Quaternion(1, 2, 3, 4)
a12 = Quaternion(5, 6, 7, 8)
a21 = Quaternion(9, 10, 11, 12)
a22 = Quaternion(13, 14, 15, 16)
b1 = Quaternion(1, 1, 1, 1)
b2 = Quaternion(1, 1, 1, 1)

a = array([
    [a11, a12],
    [a21, a22]
], dtype=Quaternion)
b = array([b1, b2], dtype=Quaternion)

s = vector_gauss(a, b)
print('в 2 примере подобрал целые части у кватернионов')
print(s)
print('проверка точности для 2 промера')
print(matmul(a, s) - b)
print('как видим точность увеличилась, но все еще далека от идеала')