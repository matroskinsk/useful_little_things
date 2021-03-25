# Числовая угадайка
from random import *

print('Добро пожаловать в числовую угадайку')
s = input('Введите верхнюю границу для угадывания числа:\n')
while not s.isdigit():
    s = input('Введите целое число:\n')
n = randint(1, int(s))
def is_valid(otvet):
    return otvet.isdigit() and int(otvet) in range(1, 101)
count = 0
Flag = True
while Flag:
    a = input(f'Введите целое число от 1 до {s}: \n')
    if not is_valid(a):
        print(f'А может быть все-таки введем целое число от 1 до {s}?')
        continue
    else:
        a = int(a)
        count += 1
        if a == n:
            print('Вы угадали, поздравляем!')
            print(f'Загаданное число = {n}, вам потребовалось {count} попыток')
            print('если хотите еще раз сыграть введите Y, если нет введите N:')
            q = ''
            while q != 'Y' or q != 'N':
                q = input()
                if q == 'Y':
                    n = randint(1, int(s))
                    count = 0
                    break
                elif q == 'N':
                    Flag = False
                    break
                else:
                    print('Введите Y или N')
        elif a < n:
            print('Ваше число меньше загаданного, попробуйте еще')
            continue
            
        elif a > n:
            print('Ваше число больше загаданного, попробуйте еще')
            continue        
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    
        
    
