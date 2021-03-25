d = []
onf = open('C:\\Users\\IKochkurov\\Desktop\\Wiev\\t_out_n.txt', 'w') # Открываем файл
with open('C:\\Users\\IKochkurov\\Desktop\\Wiev\\t_in_n.txt') as inf: # Открываем, читаем
    for line in inf:
        line = line.split() 
        d.append(line)# записываем значения из файла в список
m = [[i for j in range(2)] for i in range (1,12)]

for i in range(len(m)): # Для вывода результата
    for j in range(len(m[i])):
        m[i][1] = '-'
for i in range(len(d)): #Достаем значения из списка d и ложим в список м по классам
    for j in range(len(m)):
        if int(d[i][0]) == m[j][0]:
            m[j].append(int(d[i][2]))
for i in range(len(m)-1): # меняем значение - на средний рост у 10 классов
    if len(m[i]) > 2:
        m[i][1] = (sum(m[i][2:])/ (len(m[i]) - 2))
    onf.write((str(m[i][0]) + ' ' + str(m[i][1])) + '\n') # Пишем в файл
onf.write((str(m[10][0]) + ' ' + str(sum(m[10][2:])/ (len(m[10]) - 2))))# меняем значение - на средний рост у 11 класса и пишем в файл
onf.close


