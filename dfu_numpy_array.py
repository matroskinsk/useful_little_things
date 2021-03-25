import numpy as np
s = np.array(list(map(int, input().split())))
p = np.array(list(map(int, input().split())))
k = p / s
l_1 = len(np.where(k <= 30)[0]) * 1
l_2 = len(np.where(np.logical_and(k > 30, k <= 60))[0]) * 1.5
l_3 = len(np.where(np.logical_and(k > 60, k <= 120))[0]) * 3
l_4 = len(np.where(k > 120)[0]) * 4.5
l = l_1 + l_2 + l_3 + l_4
print('Длина пути: %3d км, оплата: %5.2f S$' % (sum(s), l))