# 1 задание
import numpy as np
import pandas as pd

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

mean_zp = np.mean(zp)
mean_ks = np.mean(ks)

# Найдем ковариацию с помощью элементарных действий:
cov = sum((zp - mean_zp) * (ks - mean_ks)) / (len(zp) - 1)
print('Ковариация:', cov)

# Найдем ковариацию с помощью функции cov из numpy:
cov_from_np = np.cov(zp, ks, ddof=1)[0, 1]
print('Ковариация с помощью numpy:', cov_from_np)

# Проверяем равенство:
assert cov == cov_from_np

# Найдем коэффициент корреляции Пирсона:
std_zp = np.std(zp, ddof=1)
std_ks = np.std(ks, ddof=1)

corr_coef = cov / (std_zp * std_ks)
print('Коэффициент корреляции Пирсона:', corr_coef)

# Найдем коэффициент корреляции Пирсона с помощью библиотек numpy и pandas:
corr_coef_from_np = np.corrcoef(zp, ks)[0, 1]
print('Коэффициент корреляции Пирсона с помощью numpy:', corr_coef_from_np)


df = pd.DataFrame({'zp': zp, 'ks': ks})
corr_coef_from_pandas = df['zp'].corr(df['ks'])
print('Коэффициент корреляции Пирсона с помощью pandas:', corr_coef_from_pandas)

# 2 задание

import scipy.stats as st

sample = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
mean = np.mean(sample)
std_err_mean = st.sem(sample)
t = st.t.ppf(1 - (1 - 0.95) / 2, len(sample) - 1)
std_err_mean = st.sem(sample)
t = st.t.ppf(1 - (1 - 0.95) / 2, len(sample) - 1)
interval_lower = mean - t * std_err_mean
interval_upper = mean + t * std_err_mean

print(f"Доверительный интервал: ({round(interval_lower,2)}, {round(interval_upper,2)})")

