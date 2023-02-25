#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cpython_arc_sin.py")
)

setup(
    ext_modules=cythonize("pyx_cpython_acr_sin.pyx")
)
