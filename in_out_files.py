d = []
with open('C:\\Users\\IKochkurov\\Desktop\\Wiev\\t_in.txt') as inf: # Открываем, читаем
    for line in inf:
        line = line.strip() 
        d.append(line)# записываем значения из файла в список
# Убираем из списка ';', баллы преобразуем в числа
for i in range(len(d)): 
    d[i] = d[i].split(';')
for i in range(len(d)):
    for j in range(1, len(d[i])):
        d[i][j] = int(d[i][j])
        

onf = open('C:\\Users\\IKochkurov\\Desktop\\Wiev\\t_out.txt', 'w') # Открываем файл
exi = '' #последняя строка вывода
s = 0
# записываем в выводной файл значение средних оценок
for i in range(len(d)):
    a = str(round(((d[i][1] + d[i][2] + d[i][3]) / 3), 9)) + '\n' 
    onf.write(a)
# записываем в выводной файл средний бал по предметам
for j in range(1, len(d[i])):
    for i in range(len(d)):
        a  = d[i][j]
        s += a
    exi += (str(round(s / len(d), 9)) + ' ')
    a = 0
    s = 0

exi = exi.rstrip()
onf.write(exi)
onf.close


