import numpy as np
import numpy.linalg as alg
#Создать двухмерный массив из вершин многоугольника
array_list = [ ]
n = int(input())
for i in range(n):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype = int)
#матрица поворота вокруг центра координат (ϕ - значение угла поворота в радианах):
ϕ = np.radians(int(input()))
rotate = ([[np.cos(ϕ), np.sin(ϕ)], [-np.sin(ϕ), np.cos(ϕ)]])  
#Умножить массив вершин на матрицу поворота. Полученная матрица - координаты вершин многоугольника после поворота
a_rotate = np.dot(a, rotate)
#Найти среднее значение первого столбца (avg_x) и среднее значение второго (avg_y)
print('avg_x = %6.2f, avg_y=%6.2f' % (sum(a_rotate[:,0]) / n, sum(a_rotate[:,1]) / n,))


