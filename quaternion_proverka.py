from quaternion import Quaternion

q = Quaternion(1, 2.0, -3, 4)
w = Quaternion(1.1 - 0.123j, 0 + 5j)
print(q)
print(w)
print()
print('сложение:', q + w, '\n')
print('обратное сложение:', 1 + q, '\n')
print('умножение:', q * w, '\n')
print('деление:', q / w, '\n')
print('обратное деление:', 2 / w, '\n')
print('возведение в степень:', q ** 3, '\n')
print('преобразование к другим классам:', float(Quaternion(1, 0, 0, 0)), '\n')
print('модуль числа:', abs(q), '\n')
