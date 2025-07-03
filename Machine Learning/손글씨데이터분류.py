### 문제정의 -손글씨 데이터를 가지고 0~9를 분류하는 모델을 만들어보기 - 이미지데이터를 학습시켜야되는데 수치형 데이터로 변환한 상태로 학습
# 데이터 수집 (생략)

#%%
import pandas as pd
# %%
import numpy as np
# %%
import matplotlib.pyplot as plt
# %%
data =pd.read_csv('./data/digit_train.csv')
# %%
data.head()
# %%
# 1. data에서 Label 컬럼 인덱싱해서 y변수에 담기
y=data['label']
# %% data에서 label을 컬럼을 제외한 나머지 칼럼들을 X변수에 담기
X=data.drop(columns=['label'])
# %%
img0 = X.iloc[0, : ].values #각 픽셀별로 0~255 숫자를 통해 밝기를 나타냄 0:검정 , 1: 흰색
# %%
img0.shape #784개의 데이터가 존재하는 1차원 배열의 형태
# %%    28*28 형태로 변환  
# 크기변환해주기 reshape 
img0_reshape = img0.reshape(28,28)  #변환된 이미지 변수로 저장
# %%
img0_reshape.shape
# %%       이미지 그려보기    ->pyplot -> plt.imshow()
plt.imshow(img0_reshape,cmap='gray')
#%% 정답확인
y[0]
# %%    train,test 데이터 셋 분리
from sklearn.model_selection import train_test_split
# %%
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=2025)
# %%
X_train.shape
# %%
X_test.shape
# %%
y_train.shape
# %%
y_test.shape
# %% 모델 선택 및 학습 진행
# -Logistic Regression
# -KNN
#%%
from sklearn.linear_model import LogisticRegression
# %%
logi_model = LogisticRegression()
# %%
logi_model.fit(X_train,y_train)
# %%
print('Logistic Regression :',logi_model.score(X_test,y_test))
# %% Confusion matrix(혼동행렬) TN FP FN TP 정확도 ,정밀도 ,재현율,재현율,민감율
# ROC curve , AUC
#%%
# 1.KNN모델 불러오기
from sklearn.neighbors import KNeighborsClassifier
# 2.KNN모델 생성
#%%
knn_model = KNeighborsClassifier()
#%%
# 3.학습
knn_model.fit(X_train,y_train)
#%%
# 4.score출력
print('KNN :',knn_model.score(X_test,y_test))
# %%
from sklearn.metrics import accuracy_score, f1_score,roc_auc_score,precision_score,recall_score
# %%
y_pred = knn_model.predict(X_test)
# %%
accuracy_score(y_test,y_pred)
# %%
