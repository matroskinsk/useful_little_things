import numpy as np
country, tourists, poly, pogr = input(), np.array(list(map(float, input().split()))), int(input()), float(input())
prog_year = 2018
year = ([i for i in range(2005, 2018)])
trande = np.polyfit(year, tourists, poly)
def get_trend(x, a, n):
    if n == 3:
        return a[0] * x ** n + a[1] * x ** (n - 1) + a[2] * x + a[3] 
    if n == 2:
        return a[0] * x ** n + a[1] * x  + a[2] 
    if n == 1:
        return a[0] * x ** n + a[1] 
prog_tourists = get_trend(prog_year, trande, poly)
pogr = (abs(prog_tourists - pogr) / pogr * 100)
print('Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц.' % (country, prog_tourists, pogr ))