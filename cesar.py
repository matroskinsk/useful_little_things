# Шифр Цезаря
s = input('Введите текст:\n')
#n = int(input('Введите значение сдвига:\n'))
s_out = ''
clv = [chr(i) for i in range(ord('а'), ord('я') + 1)]
clv_A = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
clv_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
clv_en_A = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def cesar(text, sdvig):
    s_out = ''
    for i in range(len(text)):
        if text[i] in clv:
            s_out += clv[(clv.index(text[i]) + sdvig) % 32]
        elif text[i] in clv_A:
            s_out += clv_A[(clv_A.index(text[i]) + sdvig) % 32]
        elif text[i] in clv_en:
            s_out += clv_en[(clv_en.index(text[i]) + sdvig) % 26]
        elif text[i] in clv_en_A:
            s_out += clv_en_A[(clv_en_A.index(text[i]) + sdvig) % 26]    
        else: 
            s_out += text[i]
    return s_out
count = 0
for n in range(26):
    print(count)
    print(cesar(s, n))
    count +=1
#print(cesar(s, n))