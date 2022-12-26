#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def primality_1(n):  # Теорема Ферма
    flag = True
    k = 3
    if n == 1 or n == 4:
        return not flag
    elif n == 2 or n == 3:
        return flag
    for i in range(k):
        a = randint(1, n - 1)
        if a ** (n - 1) % n != 1:  # проверяем теорему Ферма для 3 рандомных чисел
            flag = False
            break
    return flag


def primality_2(n):  # просто перебор делителей
    if n % 2 == 0:
        return n == 2
    else:
        a = 3
        while a * a <= n and n % a != 0:
            a += 2
        return a * a > n


if __name__ == '__main__':
    for i in range(2, 1000):
        if primality_1(i) != primality_2(i):  # хватает ли для теоремы Ферма проверки 3 рандомных чисел
            print(i)
