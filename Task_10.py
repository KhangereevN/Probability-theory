import numpy as np
from scipy import stats

f_data = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h_data = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
w_data = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

f, p_value = stats.f_oneway(f_data, h_data, w_data)
print('p_value =', round((p_value),4))
print('F_статистика =', round((f),4))
if p_value < 0.05:
    print("Средний рост различается в зависимости от вида спорта (гипотеза H1)")
else:
    print("Нет значительных различий в среднем росте в зависимости от вида спорта (гипотеза H0)")






