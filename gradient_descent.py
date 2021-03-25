def grad_descent_v2(func, deriv, low=None, high=None, callback=None):
    """ 
    Реализация градиентного спуска для функций с несколькими локальным минимумами,
    но с известной окрестностью глобального минимума. 
    Все тесты будут иметь такую природу.
    :param func: float -> float — функция 
    :param deriv: float -> float — её производная
    :param low: float — левая граница окрестности
    :param high: float — правая граница окрестности
    """
    # YOUR CODE
    
       
    error_list = []
    estim = []
    iter_z = 5
    iter_i = 1000
    
    np.random.seed(179)
    
    for z in range(iter_z):    
        
        estimate = np.random.uniform(low, high)
        #if abs(func(estimate)) > 10 or estimate in error_list or estimate < low or estimate > high: #отсекаем большие стартовые значения
            
           # while func(estimate) > 10:
                #error_list.append(estimate)
                #estimate = np.random.uniform(low, high)
        
                
        for i in range(iter_i):
            eps = abs(1/((deriv(estimate) + 1e-9) * (i + 1)))
            check = estimate 
            estimate -= eps * deriv(estimate)
            callback(estimate, func(estimate))
            if abs(check - estimate) < 0.001 or func(estimate) > 50:                
                break
        estim.append(estimate)
    
    best_estimate = np.random.uniform(low, high)   
    for i in range(len(estim)):
        if func(estim[i]) < func(best_estimate):
            best_estimate = estim[i]
        
    #print(best_estimate)
    return best_estimate