onf = open('C:\\Users\\IKVO\\Desktop\\PYTHON\\pt\\t_out.txt', 'w') # Открывем файл
with open('C:\\Users\\IKVO\\Desktop\\PYTHON\\pt\\t_in.txt') as inf:
    for line in inf:
        onf.write(line)
        print(line)
#onf = open('C:\\Users\\IKVO\\Desktop\\PYTHON\\pt\\t_out.txt', 'w') # Открывем файл
#onf.write(''.join(l)) # Преобразуем список в строку и записываем в файл
onf.close