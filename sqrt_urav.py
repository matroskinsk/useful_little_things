# Решение квадратного уравнения: ах2 +вх + с = 0
from math import *
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c # Находим дискриминант
if d >= 0:
    x1 = (-1 * b + sqrt(d)) / (2 * a) # Находим  x1
    x2 = (-1 * b - sqrt(d)) / (2 * a) # Находим x2
    if x1 != x2:
        print(min(x1, x2), max(x1, x2), sep='\n') # Выводим в порядке возрастания
    else:
        print(x1) # Вариант при дискриминант = 0
else:
    print('Нет корней')
    



if max(a, b, c, key=len) - ((len(a) + len(b) + len(c)) - (max(a, b, c, key=len) + min(a, b, c, key=len))) == ((len(a) + len(b) + len(c)) - (max(a, b, c, key=len) + min(a, b, c, key=len))) - min(a, b, c, key=len))