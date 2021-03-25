import matplotlib.pyplot as plt
from math import * 
#Опишем функцию:

def f_1(x):
   return e ** cos(radians(x)) + log(sin(0.8 * radians(x))**2 + 1) * cos(radians(x))
def f_2(x):
    return -1 * log((cos(radians(x)) + sin(radians(x))) ** 2 + 1.7) + 2
#Зададим начало a и конец  b интервала построения функции, задав количество точек построения. Вычислим шаг:

a = -240 # Начало интервала

b = 360 # Конец интервала

n = 100 # количество точек

h = (b-a)/(n-1) #Шаг
#Сформируем списки со значениями аргументов и значениями функции в них:

x_list = [a + h * i for i in range(n)]

f_list = [f_1(x) for x in x_list]
f_list_2 = [f_2(x) for x in x_list]
# Построим линию графика, установим для нее цвет и толщину:
plt.title('Графики функций')

line = plt.plot(x_list, f_list)
line_2 = plt.plot(x_list, f_list_2)

plt.setp(line, color="green", linewidth=2, label = 'f_1(x)')
plt.setp(line_2, color="red", linewidth=2, label = 'f_2(x)')
plt.legend()
# Выведем 2 оси, установим для них позицию zero:

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)
# Отобразим область построения:

plt.show()