import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    nobs = np.array([x_cnt, y_cnt])
    count = np.array([x_success, y_success])
    t, pval = proportions_ztest(count, nobs, value=0.1, alternative='smaller')
    #return t
    if t > -1.28:
        return True
    else:
        return False
