#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numbers import Number


class QuaternionTypeError(TypeError):
    pass


class QuaternionDomainError(ValueError):
    pass


class Quaternion(Number):
    """Кватеринионы"""

    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        if isinstance(a, complex) or isinstance(b, complex):
            self.a = a.real
            self.b = a.imag
            self.c = b.real
            self.d = b.imag
        elif isinstance(a, Number) and isinstance(b, Number) and isinstance(c, Number) and isinstance(d, Number):
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
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)

        if isinstance(other, Quaternion):
            return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d
        else:
            raise QuaternionDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)

        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        return Quaternion(a, b, c, d)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Quaternion(-1 * self.a, -1 * self.d, -1 * self.c, -1 * self.d)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)

        a1 = self.a
        a2 = other.a
        b1 = self.b
        b2 = other.b
        c1 = self.c
        c2 = other.c
        d1 = self.d
        d2 = other.d
        a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
        b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
        c = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
        d = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
        return Quaternion(a, b, c, d)

    def __rmul__(self, other):
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)

        return other.__mul__(self)

    def __abs__(self):
        return (self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2) ** 0.5

    def __truediv__(self, other):
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)
        if other.__abs__() == 0:
            raise ZeroDivisionError()
        modul2 = other.__abs__() ** 2
        a = other.a / modul2
        b = -1 * other.b / modul2
        c = -1 * other.c / modul2
        d = -1 * other.d / modul2
        return self.__mul__(Quaternion(a, b, c, d))

    def __rtruediv__(self, other):
        if isinstance(other, Number) and not isinstance(other, Quaternion):
            other = Quaternion(other)

        return other.__truediv__(self)

    def __pow__(self, power, modulo=None):
        if power == 1:
            return self
        else:
            if isinstance(power, int):
                return self.__mul__(self.__pow__(power - 1))
            else:
                raise QuaternionTypeError("You can't raise Quaternion to a not-int degree")

    def conjugate(self):  # возвращает сопряженной число
        return Quaternion(self.a, -1 * self.b, -1 * self.c, -1 * self.d)

    def __complex__(self):
        if not (self.c or self.d):
            return complex(self.a, self.b)
        else:
            raise QuaternionDomainError("Can't consider higher degree Quaternion as a complex")

    def __float__(self):
        if not (self.b or self.c or self.d):
            return float(self.a)
        else:
            raise QuaternionDomainError("Can't consider higher degree Quaternion as a float")

    def __int__(self):
        if not (self.b or self.c or self.d):
            return int(self.a)
        else:
            raise QuaternionDomainError("Can't consider higher degree Quaternion as a integrate")

    def __bool__(self):
        return self.a or self.b or self.c or self.d
