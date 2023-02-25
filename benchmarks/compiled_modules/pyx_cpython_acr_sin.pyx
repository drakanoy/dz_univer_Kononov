cdef class My_arcsin():
    cdef float[4] partial_sum, new_x, x
    cdef long long ITERATIONS, multiplier
    def __init__(self):
        self.x = 3.1415926 / 4

    def my_arcsin(self):  # считаем арксинус просто через cpython
        ITERATIONS = 100
        multiplier = 1
        partial_sum = self.x / 3.1415926 / 2
        new_x = self.x / 3.1415926 / 2
        for n in range(3, ITERATIONS, 2):
            multiplier *= (n - 2) / (n - 1)
            new_x = self.x ** n
            partial_sum += new_x / n * multiplier
        self.x = partial_sum
        return partial_sum