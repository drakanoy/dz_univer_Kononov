from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
from proverka_gauss import test_error
import timeit

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)


def vector_gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)  # concatenate заодно и скопирует
    d = len(ab)  # размер по старшему измерению

    # прямой
    for i in range(d):
        ab_ii = ab[i, i]
        j = i
        while ab_ii == 0:
            j += 1
            ab_ii = ab[j, j]
        ab[i], ab[j] = ab[j], ab[i]
        ab[i] = ab[i] / ab_ii
        for k in range(i + 1, d):
            ab[k] = ab[k] - ab[k, i] * ab[i]

    # обратный
    for i in range(d - 1, -1, -1):
        summ = 0
        for j in range(d - 1, i, -1):
            summ += ab[j] * ab[i, j]
        ab[i] = ab[i] - summ

    x = ab[:, -1]  # Последний столбец
    return x


solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution - oob_solution, ord=1))
print(test_error(vector_gauss))
# посмотрим на скорость работы ради интереса)))
print('Мой метод Гаусса', timeit.timeit(lambda: test_error(vector_gauss), number=10) / 10)
print('Встроенный метод Гаусса', timeit.timeit(lambda: test_error(solve_out_of_the_box), number=10) / 10)
