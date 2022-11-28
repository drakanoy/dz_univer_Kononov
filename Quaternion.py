#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numbers import Number
import itertools


class QuaternionTypeError(TypeError):
    pass


class QuaternionDomainError(ValueError):
    pass


class Quaternion(Number):
    """Кватеринионы"""

    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        if isinstance(a, Number) and isinstance(b, Number) and isinstance(c, Number) and isinstance(d, Number):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        elif isinstance(a, Quaternion):
            self.a = a.a
            self.b = a.b
            self.c = a.c
            self.d = a.d
        else:
            raise QuaternionTypeError(
                'You are trying to create Quaternion from ' + repr(a) + repr(b) + repr(c) + repr(d))

    def __str__(self):
        y = lambda x: '-' if x < 0 else '+'
        return str(self.a) + y(self.b) + str(abs(self.b)) + 'i' + y(self.c) + str(abs(self.c)) + 'j' + y(self.d) + str(
            abs(self.d)) + 'k'

    def __eq__(self, other):
        if isinstance(other, Number):
            other = Quaternion(other)

        if isinstance(other, Quaternion):
            return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d
        else:
            raise QuaternionDomainError("Can't say if Quaternion is equal to " + str(type(other)))
