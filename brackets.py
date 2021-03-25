# put your python co
s_in = list(input())
s_out = []
flag = True
if s_in[0] in ')]}' or s_in[-1] in'{[(':
    print('NO')
else:
    for i in range(len(s_in)):
        if s_in[i] in '([{':
            s_out.append(s_in[i]) 
            
        elif (s_in[i] == ')' and s_out[-1] == '(') and len(s_out) > 1:
            s_out.pop()
            
        elif len(s_out) > 1 and (s_in[i] == ']' and s_out[-1] == '['):
            s_out.pop()
            
        elif (s_in[i] == '}' and s_out[-1] == '{') and len(s_out) > 1:        
            s_out.pop()
        elif len(s_out) == 1 and ((s_in[i] == ')' and s_out[0] == '(') or (s_in[i] == '}' and s_out[0] == '{') or (s_in[i] == ']' and s_out[0] == '[')):
            s_out.pop()    
        else:
            flag = False
            break

    if len(s_out) == 0 and flag:
        print('YES')
    else:
        
        print('NO')