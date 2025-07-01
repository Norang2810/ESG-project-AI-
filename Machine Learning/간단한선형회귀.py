# %% DF생성을 위한 라이브러리
import pandas as pd

# %% DF생성을 위한 라이브러리
import numpy as np

# %% DF생성을 위한 라이브러리
import matplotlib.pyplot as plt

# %% 성적 데이터를 담은 DF생성
# index지정['은유', '자영', '지희', '영화']
# columns지정['시간', '성적']
# data 변수에 저장
data  = pd.DataFrame(data :{[2, 20], [4, 40], [8, 80], [9, 90] },
    index=["은유", "자영", "지희", "영화"],
    columns=["시간", "성적"],
)

# %%
