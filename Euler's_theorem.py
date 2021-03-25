import time
from math import ceil
start_time = time.time()
flag = False


total_oper = 0
for a in range(1, 151):
    if flag == True:
        break
    for b in range(1, 151):
        if flag == True:
            break
        for c in range(1, 151):
            if flag == True:
                break
            for d in range(1, 151):
                if flag == True:
                    break
                for e in range (1, 151): 
                    total_oper += 1 
                    
                    if a**5 + b**5 + c**5 + d**5 - e** 5 == 0 and a < b < c < d < e:
                        print('------------------', a, b, c, d, e )
                        flag = True
                        print(ceil(time.time() - start_time)//60, 'минут', ceil(time.time() - start_time), 'секунд')
                        print(total_oper)
                        break
                        
                        
