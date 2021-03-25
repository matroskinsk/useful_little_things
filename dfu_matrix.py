#Подключить модули  numpy и  numpy.linalg:

import numpy as np

import numpy.linalg as alg
#Создать матрицу A в виде двухмерного массива, вывести ее на экран («\n» используется для перехода на следующую строку при выводе):

a = np.array([[3, 4, -2],[-2, -1, 4],[1, 2, 1]]) 
#array_list = [ ]
#for i in range(n):
#    line = input()
#    array_str = line.split()
#    array_list.append(array_str)
#a = np.array(array_list, dtype = int)


print("A :\n", a)
#Создать матрицу B , вывести ее на экран :

b = np.array([[1, -3, -2, 1],[2, 4, -2, -1],[5, -2, 0, -2]])

print("B :\n", b)
#Вычислить произведение A и B, вывести результат:

c = np.dot(a, b)

print("A*B:\n", c)
#Вычислить определитель матрицы A, вывести результат:

det_a = alg.det(a)

print("dеt(A): ", round(det_a, 1))
#Вычислить обратную матрицу A-1:

a_inv = alg.inv(a)

print("A^-1:\n", np.round(a_inv,1))
#Вычислить матричное выражение   


a_3 = np.dot(a, np.dot(a,a))

result = det_a * np.dot(a_inv, b) - 10 * np.dot(a_3, b)

print("Result:\n", result)
#### Подключить модули  :
  


# Вычислить сумму элементов главной диагонали.матрицы A, вывести результат:

sum_diag = np.sum(np.diag(a))

print("sum_diag =  ", sum_diag)
# Найти максимальные элементы каждого столбца:

max_col = np.max(a, 0)

print("max_col :", max_col)
#Найти минимальные элементы каждой строки:

min_row = np.min(a, 1)

print("min_row :", min_row)
