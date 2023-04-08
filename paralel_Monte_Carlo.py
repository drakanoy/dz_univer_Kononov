import numpy as np
from multiprocessing import Pool, freeze_support
import time


def worker(l1):
    seed, a, b, f = l1
    np.random.seed(seed)
    x = np.random.uniform(a, b, len(a))  # генерируем случайную точку
    return f(x)  # вычисляем значение функции в точке


def monte_carlo_integration(f, a, b, n, num_procs=4):
    """
    f - функция, которую необходимо интегрировать
    a, b - массивы пределов интегрирования в каждом измерении
    n - количество точек, используемых в методе Монте-Карло
    num_procs - количество процессов, используемых для вычислений
    """
    pool = Pool(num_procs)  # создаем пул процессов
    results = []

    for i in range(num_procs):
        seeds = np.random.randint(0, 2 ** 31 - 1, n // num_procs)  # генерируем seed для каждого процесса
        l1 = [(seed, a, b, f) for seed in seeds]
        result = pool.map(worker, l1)  # запускаем процессы на выполнение
        results.append(sum(result))

    pool.close()
    pool.join()

    volume = np.prod(np.array(b) - np.array(a))  # объем гиперкуба
    approx_integral = volume * sum(results) / n  # вычисляем приближенное значение интеграла
    return approx_integral


# Пример использования
def paraboloid(x):
    return x[0] ** 2 + x[1] ** 2


if __name__ == '__main__':
    freeze_support()
    a = [-1, -1]  # пределы интегрирования
    b = [1, 1]
    n = 10_000_000  # количество точек
    num_procs = 8  # количество процессов
    start_time = time.time()
    result = monte_carlo_integration(paraboloid, a, b, n, num_procs)
    stop_time = time.time()
    print(str(n) + ';', str(num_procs) + ';', str(result) + ';', str(stop_time - start_time))  # выводим приближенное значение интеграла
