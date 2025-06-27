# %%
# 모델이 공부할 재료 - > 학습 데이터가 필요
# 학습 데이터를 생성
# numeric python -> numpy
# 표 -> DataFrame     pandas

# %%
import numpy as np
# %%
import pandas as pd
# %%
import matplotlib.pyplot as plt
# %%  지도학습 ,분류 모델
# 1,0 : 수치형 데이터처럼 보이지만! 범주형
# 혈액형
# 1: A형, 2: B형, 3: O형, 4: AB형
# 딕셔너리를 전달인자로 넘겨서 DataFrame 생성
# pandas안에 있는 DataFrame이라는 함수 호출
# %%
data = pd.DataFrame({'A':[0,0,1,1,1,0,1,0],
                'B':[0,1,0,1,0,0,1,1],
                'A and B':[0,0,0,1,0,0,1,0]})
print(data)
# %% 데이터 분리
# 정답데이터(y)와 특성데이터(X)를 분리
# 컬럼 인덱싱 : 원하는 컬럼을 선택해서 가져올것임
y = data['A and B']  # 정답 데이터
X = data[['A', 'B']]  # 두개이상의 컬럼을 가져오기 위해 리스트([])로 묶어줌
# %%
X
# %%
# 학습용 데이터와 테스트용 데이터로 분리
# 학습데이터 -> X,Y 에서 0~5번째 (포함) 행까지 잘라서 학습데이터로 사용
X_train = X.iloc[:6]  # 학습용 데이터
y_train = y.iloc[:6]  # 학습용 정답 데이터

# %% 테스트데이터 ->X,y 에서 6~7번째 (포함) 행까지 잘라서 테스트용 데이터로 사용
X_test = X.iloc[6:]  # 테스트용 데이터
y_test = y.iloc[6:]  # 테스트용 정답 데이터
# %%
print(X_train.shape) #shpae는 DataFrame의 모양을 담고있는 속성
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
# %% 머신러닝 모델 : KNN을 학습시킬예정
# KNN 모듈 설치 명령어 (터미널/명령 프롬프트에서 실행)
# !pip install scikit-learn

# %%
from sklearn.neighbors import KNeighborsClassifier
# KNeighborsClassifier : KNN 분류 모델
# Regressor : KNN 회귀 모델
#%%
knn_model = KNeighborsClassifier(
    n_neighbors=1  # KNN에서 K의 값, 몇개의 이웃을 참고할지
)
# %% 모델 학습(fit)
knn_model.fit(X_train, y_train)  # 학습용 데이터로 모델 학습
# %% 평가
# 예측 -> predict
y_pred = knn_model.predict(X_test)  # 테스트용 데이터로 예측
# %% 예측 결과
print("예측 결과:", y_pred)
# 정답 데이터와 예측 결과 비교
print("정답 데이터:", y_test.values)
# 평가
# score : 정확도
knn_model.score(X_test, y_test)  # 테스트용 데이터로 정확도 평가

# 과대적합 : 모델이 학습용 데이터에 너무 과하게 적합되어
#            테스트용 데이터에 대한 일반화 성능이 떨어지는 현상
# 과소적합  : 모델이 학습용 데이터에 충분히 적합되지 않아
#            학습용 데이터와 테스트용 데이터 모두에 대한 성능이 떨어지는 현상
# 일반화 : 모델이 학습용 데이터에 적합하면서도
#            테스트용 데이터에 대해서도 좋은 성능을 내는 것
# 과대적합과 과소적합을 피하는 것이 중요하다.

# 일반화 성능을 높이기 위해서는 
# 1. 충분한 양의 학습 데이터를 확보해야 한다.
# 2. 모델의 복잡도를 조절해야 한다.
# 3. 적절한 하이퍼파라미터를 설정해야 한다.


# 최근접 이웃 알고리즘
# KNN은 가장 가까운 K개(홀수 권장)의 이웃을 찾아서
# 그 이웃들의 클래스(범주)를 투표하여 예측하는 알고리즘이다.
# KNN은 간단하고 직관적인 알고리즘으로
# 분류와 회귀 문제에 모두 사용할 수 있다.

# 유클리드 거리
# KNN은 유클리드 거리를 사용하여
# 데이터 포인트 간의 거리를 계산한다.
# 유클리드 거리는 두 점 사이의 직선 거리를 계산하는 방법이다.
# 유클리드 거리 공식:
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# 맨해튼 거리
# KNN은 맨해튼 거리도 사용할 수 있다.   
# 맨해튼 거리는 두 점 사이의 수평 거리와 수직 거리의 합을 계산하는 방법이다.
# 맨해튼 거리 공식:
# d = |x2 - x1| + |y2 - y1|

# KNN의 하이퍼파라미터
# 1. K: 가장 가까운 이웃의 개수
# 2. 거리 측정 방법: 유클리드 거리, 맨해튼 거리 등
# 3. 가중치: 이웃의 거리에 따라 가중치를 부여할지 여부
# %%