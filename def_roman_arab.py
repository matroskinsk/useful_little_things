def arab(n):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tmp = []
    x = 0
    n = list(n)
    for i in range(len(n)):
        tmp.append(d[n[i]])
    while len(tmp) != 0:
        if len(tmp) > 1 and tmp[-1] > tmp[-2]:
            x += tmp[-1] - tmp[-2]
            tmp.pop()
            tmp.pop()
        else:
            x += tmp[-1]
            tmp.pop()        
    return x