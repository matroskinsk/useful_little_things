#1. Импортируем модуль numpy, дадим ему имя np

import numpy as np
import matplotlib.pyplot as plt
from math import ceil
#2. Сформируем массивы координат движения снаряда:

x, y, x_m, y_m = np.array(list(map(float, input().split()))), np.array(list(map(float, input().split()))), float(input()), float(input())
#3. Построим траекторию движения снаряда, используя в качестве линии тренда полином второй степени. Найдем его коэффициенты:


#4. Создадим функцию для вычисления значений полинома второй степени в точке x, разместим ее в начале программы, после импорта модуля:

tr = np.polyfit(x, y, 2)
def get_trend(x, a):
    return a[0] * x ** 2 + a[1] * x + a[2]
x_trend = [i for i in range(0, ceil(x_m) + 50, 10)]    
y_trend = [get_trend(x, tr) for x in x_trend]

h_gun = get_trend(0, tr)
h_m = get_trend(x_m, tr)
delta = abs(y_m - h_m)
def yes_no(h):
    if h <= 0.5:
        return('yes')
    else:
        return 'no'

plt.plot(x, y, 'go', label = 'положение снаряда')
plt.plot(x_trend, y_trend, 'r-', label = 'линия тренда')
plt.gca().spines['left'].set_position('zero')
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.plot(x_m, y_m, 'b+', label = 'Мишень',  c ='b', markersize = 12)
plt.legend(loc="lower center")
plt.show()

# строка форматного вывода
print('h0 = %6.2f, %2s' % (h_gun, yes_no(delta)))