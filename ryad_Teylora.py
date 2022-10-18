import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 100


def my_arcsin(x):  # считаем арксинус. эта функция подходит для -1<=x<=1
    """
    Вычисление Арксинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    эта функция подходит для -1<=x<=1
    """
    multiplier = 1
    partial_sum = x
    new_x = x
    for n in range(3, ITERATIONS, 2):
        multiplier *= (n - 2) / (n - 1)
        new_x = x ** n
        partial_sum += new_x / n * multiplier
    return partial_sum


help(math.asin)
help(my_arcsin)

print(math.asin(0.4))  # сравним значения
print(my_arcsin(0.4))

vs = np.vectorize(my_arcsin)
print(my_arcsin, vs)

angles = np.r_[-1.01:1.01:0.0001]
plt.plot(angles, np.arcsin(angles), linewidth=3.0, color='cyan', label='библиотечный арксинус')  # построим графики
plt.plot(angles, vs(angles), linewidth=1.0, color='black', label='мой арксинус')
plt.legend()
plt.show()
