#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit

from acr_sin_python import My_arcsin as My_arcsin0
from benchmarks.compiled_modules.cpython_arc_sin import My_arcsin as My_arcsin1
# from benchmarks.compiled_modules.pyx_cpython_acr_sin  import My_arcsin as My_arcsin2
from benchmarks.compiled_modules.mypy_arc_sin import My_arcsin as My_arcsin3
from numba_arc_sin import My_arcsin as My_arcsin4


def load(fate_class):
    f = fate_class()
    for _ in range(1_000_000):
        r = f.my_arcsin()
    return r


def test(fate_class):
    f = fate_class()
    for _ in range(1_000):
        r = f.my_arcsin()
    return r


for fc in [My_arcsin0, My_arcsin1, My_arcsin3, My_arcsin4]:
    print(fc, test(fc), timeit.timeit(lambda: load(fc), number=10) / 10)
