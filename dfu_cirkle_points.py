import numpy as np
a_l = []
len_points = []
n= int(input())
for i in range(n):
    a_l.append(input().split())             
points = np.array(a_l, dtype = float)
sr_points = ([sum(points[:,0] / n), sum(points[:,1] / n)])
def len_a_b(x_1, x_2, y_1, y_2):
    return ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
for i in range(n):
    len_points.append(len_a_b(sr_points[0],points[i,0], sr_points[1], points[i,1]))
print('О(%6.3f, %6.3f), r = %6.3f' % (sr_points[0], sr_points[1], max(len_points)))


