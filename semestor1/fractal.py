#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as tl


def draw_partial_fern(size, angle, c1, c2):  # c1 и с2 размеры веточек
    tl.left(angle)
    draw_fern(size * c1)
    tl.right(angle)
    tl.backward(size * c2)


def draw_fern(size):
    if size > 1:
        tl.forward(size)
        draw_partial_fern(size, 5, 0.8, 0.05)
        draw_partial_fern(size, -40, 0.45, 0.2)
        draw_partial_fern(size, 35, 0.4, 0.75)


tl.color("blue")
tl.speed(10000000)
tl.hideturtle()
tl.left(90)
draw_fern(60)
