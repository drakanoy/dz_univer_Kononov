#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = egcd(b % a, a)
    return (div, y - (b // a) * x, x)


a = int(input())
b = int(input())
print(gcd(a, b))
print(math.gcd(a, b) == gcd(a, b))  # проверка с бибеотекой math

d, x, y = egcd(a, b)
print(d == gcd(a, b))  # проверка на одинаковость наибольших делителей
print(d, x, y)
print(d == a * x + b * y)  # проверка равно ли разлодение самому делителю
