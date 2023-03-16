import numpy as np
from scipy import integrate


def monte_carlo_integration(f, a, b, N):
    """
    f - функция, которую необходимо интегрировать
    a, b - массивы пределов интегрирования в каждом измерении
    N - количество точек, используемых в методе Монте-Карло
    """
    dims = len(a)  # количество измерений
    total_integrals = 0

    for i in range(N):
        xi = np.random.uniform(a, b, dims)  # генерируем случайные точки
        total_integrals += f(xi)  # вычисляем значение функции в точке   f(xi[0], xi[1])

    volume = 1
    for i in range(dims):
        volume *= b[i] - a[i]

    result = total_integrals / N * volume  # вычисляем приближенное значение интеграла
    return result


# Пример использования
def paraboloid(x):  # функция от списка переменных, так как мой метод Монте-Карло для любого количества измерений
    return x[0] ** 2 + x[1] ** 2


def paraboloid2(x, y):  # это та же самая функция, но мы передаем 2 переменные, а не список переменных
    return x ** 2 + y ** 2  # это нужно для того, что бы считать интеграл через библиотеку


if __name__ == '__main__':
    a = [-1, -1]  # пределы интегрирования
    b = [1, 1]
    N = 100000  # количество точек

    approx_integral = monte_carlo_integration(paraboloid, a, b, N)
    print(approx_integral, 'метод Монте-Карло')  # выводим приближенное значение интеграла
    v, err = integrate.nquad(paraboloid2, [(-1, 1), (-1, 1)])
    print(v, err, 'библиотечный интеграл и его ошибка')
    print(abs(approx_integral - v), 'ошибка метода Монте-Карло')
