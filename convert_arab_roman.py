def roman(n):
    roman_dict_1 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''}
    roman_dict_10 = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 0: ''}
    roman_dict_100 = {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 0: ''}
    roman_dict_1000 = {1000: 'M'}
    n_1000 = n // 1000 * 1000
    n_100 = n % 1000 // 100 * 100
    n_10 = n  % 100 // 10 * 10
    n_1 = n % 10
    if n > 999:
        return (roman_dict_1000[1000] * (n_1000//1000) + roman_dict_100[n_100] + roman_dict_10[n_10] + roman_dict_1[n_1])    
    elif 999 >= n > 99:
        return (roman_dict_100[n_100] + roman_dict_10[n_10] + roman_dict_1[n_1])
    elif 99 >= n > 9:
        return (roman_dict_10[n_10] + roman_dict_1[n_1])
    elif 9 >= n > 0:
        return (roman_dict_10[n_10] + roman_dict_1[n_1])
n = int(input('введите число или 0 для остановки:\n'))
while n != 0:
    
    print(f'Число {n} в римской системе исчисления = {roman(n)}')
    n =  int(input('введите число или 0 для остановки:\n'))
        
        
    

