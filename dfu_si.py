# Теплопроводность кремния
import matplotlib.pyplot as plt
def compute_lambda(t): # функция вычисления теплопроводности
    b = 33
    l_0 = 884
    t_0 = 100
    y = b * l_0 /(t-t_0)
    return y
t_list = []
lambda_exp_list =[]
with open('lambda_exp.txt') as inf:
    for line in inf:
        t_lambda_list = line.split()
        t_list.append(float(t_lambda_list [0]))
        lambda_exp_list.append(float(t_lambda_list [1]))# записываем значения из файла в список
# Борода
#t_list = t_list[1:13]
#lambda_exp_list = lambda_exp_list[1:13]

# Границы температур интервала   
t1=float(input("t1 = "))
t2=float(input("t2 = "))
while (t2 <= t1 or t1 <= 99):
    print("Неверные границы температур")
    t1=float(input("t1 = "))
    t2=float(input("t2 = "))
# количество значений на интервале и посчитать шаг изменения температуры;
n = 20
h =(t2 - t1) / (n - 1)
# список со значениями температур на интервале и список значений теплопроводности
#t_list = [t1 + i * h for i in range(0,n)] # Если не читаем из файла
lambda_list = [compute_lambda(t) for t in t_list]
#тносительную погрешность вычисления теплопроводности для каждого значения температуры.
error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i] ) for i in range(len(t_list))]
max_error = max(error_list)
index_max_error = error_list.index(max_error)
min_error = min(error_list)
index_min_error = error_list.index(min_error)
avg_error = sum(error_list) / len(t_list)
# результаты, используя форматный вывод
#print('-' * 27)
#print(f'| # |{"t":^10}|{"L(t)":^10}')
#print("-" * 27)
#for i in range(len(t_list)):
#    if (i+1) < 10:
#        print(f'|  {i+1}|{t_list[i]:^10.3f}|{lambda_list[i]:^10.3f}|')
#    else:
#        print(f'| {i+1}|{t_list[i]:^10.3f}|{lambda_list[i]:^10.3f}|')
#print("-" * 27)

print("-" * 40)
print("|%7s | %7s | %7s |%8s |" % ("t","l(t)","exp(t)", "error"))
print( "-" * 40)
for i in range(len(t_list)):
    print("|%7d | %7.3f | %7.1f |%7.2f%% |" % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))
print("-" * 40) 
print("Максимальная погрешность = %5.2f%%  при t = %5d" % (max_error * 100, t_list[index_max_error]))
print("Минимальная погрешность = %5.2f%%  при t = %5d" % (min_error * 100, t_list[index_min_error]))
print("Средняя погрешность = %5.2f%%" % (avg_error * 100))
# создать линии для отображения экспериментальных и теоретических значений теплопроводности.
# Установить для них цвет, стиль и толщину, а также подпись для легенды
line_th = plt.plot(t_list, lambda_list, label = 'теоретические')
line_exp = plt.plot(t_list, lambda_exp_list, label = 'экспериментальные')
# задаем стили для линий
plt.setp(line_exp, color= "blue", linestyle = "--", linewidth = 2 )
plt.setp(line_th, color= "red", linewidth = 2)
#Вывести легенду, изменить положение осей, скрыть две из них, вывести заголовок и отобразить графики
plt.legend()
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.title("Значения теплопроводности")
plt.show()