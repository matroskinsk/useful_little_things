from math import sqrt, acos, degrees
#2. Реализовать функцию для вычисления длины отрезка с координатами концов (x0, y0) и (x1, y1).


def compute_len(x_0,y_0,x_1,y_1):
    
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    
    return len_line
#3. Реализовать функцию для вычисления площади треугольника по трем сторонам a_1, a_2, a_3.

def compute_area(a_1, a_2, a_3):
    
    p = (a_1 + a_2 + a_3) / 2
    
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    
    return area
#4. Реализовать функцию для вычисления угла треугольника в градусах, если известны длины сторон a_1, a_2, a_3.

def compute_angle(a_1, a_2, a_3):
    
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2)/
                     (2 * a_1 * a_2))
    
    return degrees(angle_rad)
    
#радиус вписанной окружности
def round_in(a, b, c):
    p = a + b + c
    r = ((p / 2 - a) * (p / 2 - b) * (p / 2 - c) / (p / 2)) ** 0.5
    return r
# Радиус описанной окружности
def round_out(a, b, c):
    p = (a + b + c) / 2
    x = sqrt(p * (p - a) * (p - b) * (p - c))
    s = (a * b * c) / (4 * x)
    return s
# сумма мередиан
def sum_mer(a, b, c):
    m_a = 0.5 * sqrt( 2 * (c ** 2 + b ** 2) - a ** 2)
    m_b = 0.5 * sqrt( 2 * (c ** 2 + a ** 2) - b ** 2)
    m_c = 0.5 * sqrt( 2 * (a ** 2 + b ** 2) - c ** 2)
    return m_a + m_b + m_c
#5. Ввести координаты вершин треугольника с подсказкой пользователю.

x_a = float(input("x_a = "))

y_a = float(input("y_a = "))

x_b = float(input("x_b = "))

y_b = float(input("y_b = "))

x_c = float(input("x_c = "))

y_c = float(input("y_c = "))
#6. Вычислить длины сторон треугольника.

c = compute_len(x_a, y_a, x_b, y_b)

a = compute_len(x_b, y_b, x_c, y_c)

b = compute_len(x_a, y_a, x_c, y_c)
#7. Проверить, существует ли треугольник, построенный по заданным точкам, если нет - выдать сообщение пользователю.

if a + b <= c or b + c <= a or a +c <= b:
    
    print("Треугольник не существует")

#8. В противном случае вычислить площадь, периметр, величины углов.

else:     
    s = compute_area(a, b,c)
    
    p = a + b + c
    
    angle_A = compute_angle(c, b, a)
    
    angle_B = compute_angle(c, a, b)
    
    angle_C = compute_angle(a, b, c)
#9. Вывести результаты вычисления на экран, округлив их до 3-х знаков после запятой.

    print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))

    print("Площадь : ", round(s,3))

    print("Периметр : ", round(p,3))

    print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))