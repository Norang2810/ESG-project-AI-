#%%
import numpy as np
# %%
import matplotlib.pyplot as plt
# %%
import pandas as pd
# %%
import seaborn as sns
# %%
# 시각화 폰트설정
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)  # 음수 부호 깨짐 방지
# %%Con04_전국야영(캠핑)장표준데이터.csv
pd.read_csv('C:\\Users\\zhdzh\\Downloads\\KDC_데이터분석_데이터\\Con04_전국야영(캠핑)장표준데이터.csv', encoding='utf-8')  # iris 데이터셋