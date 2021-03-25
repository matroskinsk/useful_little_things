# generation password
from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
isk = 'il1Lo0O'
chars = ''
print('Эта программа сгенерирует безопасный пароль')
n = input('Какое колличество паролей необходимо сгенерировать:\n')
if not n.isdigit():
    while not n.isdigit():
        n = input('Введите целое число:\n')
l = input('Введите длинну пароля:\n')
if not l.isdigit():
    while not l.isdigit():
        l = input('Введите целое число:\n') 
        
ci = input('Будет ли пароль включать цифры "0123456789"?(д / н):\n')
if ci != 'д' and ci != 'н':
    while ci != 'д' and ci != 'н':
        ci = input('введите д или н:\n')
if ci == 'д':
    chars += digits
c_A = input('Будет ли пароль включать заглавные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?(д / н):\n')
if c_A != 'д' and c_A != 'н':
    while c_A != 'д' and c_A != 'н':
        c_A = input('введите д или н:\n')
if c_A == 'д':
    chars += uppercase_letters
c_a = input('Будет ли пароль включать строчные буквы "abcdefghijklmnopqrstuvwxy"?(д / н):\n')
if c_a != 'д' and c_a != 'н':    
    while c_a != 'д' and c_a != 'н':
        c_a = input('введите д или н:\n')
if c_a == 'д':
    chars += lowercase_letters
c_s = input('Будет ли пароль включать символы"!#$%&*+-=?@^_"?(д / н):\n')
if c_s != 'д' and c_s != 'н':    
    while c_s != 'д' and c_s != 'н':
        c_s = input('введите д или н:\n') 
if c_s == 'д':
    chars += punctuation
c_is = input('Исключить неоднозначные символы?"il1Lo0O"?(д / н):\n')        
if c_is != 'д' and c_is != 'н':    
    while c_is != 'д' and c_is != 'н':
        c_is = input('введите д или н:\n')
chars = list(chars)
if c_is == 'д':
    for i in range(len(isk)):
        chars.pop(chars.index(isk[i]))
chars = ''.join(chars)

def gen_pasw(length, chars):
    return ''.join(sample(chars, length))
onf = open('C:\\Users\\IKochkurov\\Desktop\\Wiev\\you_password.txt', 'w') # Открываем файл
for i in range(int(n)-1):
    onf.write(gen_pasw(int(l), chars) + '\n')
onf.write(gen_pasw(int(l), chars))   
onf.close
if int(n) > 1:
    print('Пароли успешно записаны в файл "you_password.txt"')
else:
    print('Пароль успешно записан в файл "you_password.txt"')
