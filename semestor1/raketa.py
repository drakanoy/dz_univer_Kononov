#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from matplotlib import pyplot as pp
import numpy as np

MODEL_G = 9.81
MODEL_DT = 0.001


class Body:
    def __init__(self, x, y, vx, vy):
        self.name = 'telo'
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y, M0, μ, u, β):
        """
        Создать ракету.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        M0: float
            начальная масса
        μ: float
            скорость изменения массы
        u: float
            скорость выпускания газов
        β: float (градусы)
            угол сопла (отсчитывается против часовой стрелки от отрицательного направления Ох)
            влево = 0
            вниз = 90
            вправо = 180
            и тд

        """
        super().__init__(x, y, 10, 10)  # Вызовем конструктор предка — тела, т.к. он для ракеты актуален
        self.name = 'raketa'
        self.M = M0
        self.μ = μ
        self.u = u
        self.β = math.radians(β)

    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        if self.M > 0:  # Горим пока есть масса
            '''Уравнени Мещерского наше всё'''
            'Всё про Ох'
            self.x += self.vx * MODEL_DT
            dvx = self.u * math.cos(self.β) * self.μ * MODEL_DT / self.M
            self.vx += dvx

            'Всё про Оy'
            self.y += self.vy * MODEL_DT
            dvy = self.u * math.sin(self.β) * self.μ * MODEL_DT / self.M - MODEL_G * MODEL_DT
            self.vy += dvy

            'Всё про массу'
            self.M -= self.μ * MODEL_DT
        else:  # Потом летим как ёжик
            super().advance()


if __name__ == '__main__':
    b = Body(0, 0, 9, 9)
    r = Rocket(x=0, y=0, M0=100, μ=10, u=100, β=45)

    bodies = [b, r]
    # Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
    # благодаря возможностям ООП будем просто работать со списком тел

    for t in np.arange(0, 10, MODEL_DT):  # для всех временных отрезков
        for b in bodies:  # для всех тел
            b.advance()  # выполним шаг

    for b in bodies:  # для всех тел
        pp.plot(b.trajectory_x, b.trajectory_y, label=b.name)  # нарисуем их траектории
    pp.legend()
    pp.show()
