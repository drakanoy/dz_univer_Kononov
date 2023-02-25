# cython: language_level=3

class My_arcsin():
    def __init__(self):
        self.x: float = 3.1415926 / 4

    def my_arcsin(self) -> float:  # считаем арксинус просто через cpython
        ITERATIONS: int = 100
        multiplier: int = 1
        partial_sum: float = self.x / 3.1415926 / 2
        new_x: float = self.x / 3.1415926 / 2
        for n in range(3, ITERATIONS, 2):
            multiplier *= (n - 2) / (n - 1)
            new_x = self.x ** n
            partial_sum += new_x / n * multiplier
        self.x = partial_sum
        return partial_sum
