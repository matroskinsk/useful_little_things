#График роста населения планеты
import matplotlib.pyplot as plt 

def f_x(x, y):
    import math
    y_list = []
    for i in range(x, y + 1):
        y_list.append(((172000000000/45)*(math.pi / 2 - math.atan((2000 - i) / 45))/1000000000) )
    return  y_list
#область определения функций
x, y, z = 1960, 1970, 3.5
#Сформируем списки со значениями аргументов и значениями функции в них:
x_list = [i for i in range(x, y + 1)]
y_list = f_x(x, y)

# Построим линии графика, установим для нее цвет и толщину:
line = plt.plot(x_list, y_list)
line_2 = plt.plot([x, y], [z, z])
plt.setp(line, color="green", linewidth=2)
plt.setp(line_2, color="red", linewidth=2)
# Выведем 2 оси, установим для них позицию zero:

plt.gca().spines["left"].set_position('center')
plt.gca().spines["bottom"].set_position('center')
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
# Отобразим область построения:
plt.show()