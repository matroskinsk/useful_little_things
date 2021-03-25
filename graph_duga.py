from matplotlib.patches import Wedge, Arc
import matplotlib.pyplot as plt
#вставить необходимые операторы
n = 6 # размер области

m  = 5# размер области

plt.xlim(0, n)

plt.ylim(0,m)

ax = plt.gca()
# нарисовать сектор
figure_w = Wedge((3, 1), 2, 45, 135)# сформировать сектор, параметры для цвета линии и заливки, а также толщины линии не указывать
ax.add_patch(figure_w)

# нарисовать дугу
# дуга должна иметь определенную толщину (linewidth = 3), нулевой угол поворота, цвет не указывать
figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3) # сформировать дугу
ax.add_patch(figure_a)

plt.show()