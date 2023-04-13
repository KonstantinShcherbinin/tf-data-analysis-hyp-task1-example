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
    #nobs = np.array([x_cnt, y_cnt])
    #count = np.array([x_success, y_success])
    nobs = y_cnt
    count = y_success
    value = x_success / x_cnt
    t, pval = proportions_ztest(count, nobs, value=value, alternative='smaller')
    #return t, pval
    if pval < 0.1:
        return True
    else:
        return False
