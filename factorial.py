#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools


class Factorial:
    """По объектам этого класса можно итерироваться и получать много факториалов"""

    class _Factorial_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self.n = 1  # первый факториал
            self.i = 0  # счётчик

        def __next__(self):
            self.i += 1
            self.n *= self.i
            return self.n

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Factorial._Factorial_iter()


if __name__ == '__main__':
    f = Factorial()
    for i in itertools.islice(f, 1000):
        print(i)
