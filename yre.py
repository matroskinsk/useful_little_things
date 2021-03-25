from math import *
x = 8
#flag = False
while True:
    s = 8 * x ** 1 + 8 * x ** 0 
    s_1 = (3 * x ** 1 + 2 * x **0) + (2 * x ** 1 + 2 * x **0) +  (1 * x ** 1 + 6 * x **0) + (1 * x ** 1 + 7 * x **0)
    if s == s_1:
        #flag = True
        print(x)
        break
    else:
        x += 1
print(e)