#Продолжаем решать задачу о движении автомобиля, код программы для частей 1-3:

import numpy as np

path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5])

speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])

len_path = path.sum()

print("Расстояние между пунктами А и В :", len_path)

time = path / speed
print("Время на каждом участке :", np.round(time, 2))

sum_time = time.sum()
print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time
print("Средняя скорость : ", round(avg_speed, 2))
#2. Вычислим максимальное время и выведем номера участков дороги, на проезд по которым потрачено больше всего времени:

max_time = time.max()

max_path = np.where(time == max_time)[0]

print("Участки, на проезд по которым потрачено больше всего времени :", max_path)
#3. Посчитаем длину и время проезда по первым 4-м участкам:

len_path_four = path[:4].sum()

print("Длина первых четырех участков :", len_path_four)

time_four = path[:4] / speed[:4]

sum_time_four = time_four.sum()

print("Время проезда :", round(sum_time_four, 2))
#4. Вычислим среднюю скорость движения по первым четырем участкам:

avg_speed_four = len_path_four / sum_time_four

print("Средняя скорость движения :", round(avg_speed_four, 2))