"""
인공지능 7과정
1.문제정의
2.데이터수집
3.전처리
4.탐색적 데이터 분석 (EDA)
5.모델선택 및 하이퍼파라미터 조정
6.모델학습(.fit())
7.모델평가(예측및 평가)
"""

# 1.문제정의
# 보스턴 주택 가격 데이터를 사용해서 주택 가격을 예측
# 집값 : 수치형 데이터
# 지도 학습
# 회귀
# %%
import pandas as pd

# %%
boston_df = pd.read_csv("./data/boston_housing.csv")
# %%
import numpy as np

# %%
import matplotlib.pyplot as plt

# %%
boston_df.info()
# %%
boston_df.isnull().sum()  # 각 컬럼의 결측치의 개수
# %%
boston_df.head()
# %% CHAS ,RAD 에 어떤값이 들어있는지 살펴보기
boston_df["CHAS"].unique()
# %% 타입변경후 변경된타입을 변수로 지정하기.
boston_df["CHAS"] = boston_df["CHAS"].astype("int")
# %% 타입 변경된지 확인
boston_df["CHAS"].dtype
# %%
boston_df["RAD"].unique().astype("int64")
# %%
boston_df["RAD"].dtype
# %%
print(boston_df["RAD"].dtype)
# %% target변수 저장
y = boston_df["MEDV"]
# %%
y.name = "PRICE"
# %% 의미없는 컬럼 drop
boston_df.columns
# %%
boston_df = boston_df.drop(columns=["Unnamed: 0"])
# %%
boston_df.info()
# %% 'MEDV'
# boston_df에서 'MEDV' 컬럼을 drop
boston_df.drop(columns=["MEDV"])
# %%
# 나머지 컬럼들은 문제데이터 X
boston_df.info()
# %%
# boston_df에서 'MEDV' 컬럼을 drop => X에대입
X = boston_df
# X.info()
# %%
y.info()
# %%
X.info
# %%
print(y.shape, X.shape)
# %% 분리한 데이터 합체하기
total = pd.concat([X, y], axis=1)
# %% EDA 탐색적 데이터 분석
# 1.상관관계분석
# -피어슨 상관계수 : 두 컬럼의 선형도 판단
total.corr()  # correlation : 상관관계
# 다른 컬럼들과의 관계를 파악하는 용도
# %% 관계를 시각화
import seaborn as sns

# %%
plt.figure(figsize=(12, 12), facecolor="black")
sns.heatmap(total.corr(),annot=True) #annot=True 수치값을 그래프에 표기
plt.show()
#  열 간의 상관관계를 -1~1 사이의 값으로 나타냄 : 피어슨 상곤계수
# %%%1에 가까울수록 양의 상관관계 , -1에 가까울수록 음의 상관관계
# heatmap() : 시각적으로 뚜렷한 차이를 확인
# 데이전처리 하기전 우선순위를 판단하는 근거로 사용
# 모델 학습하는데 시간이 너무 오래걸림 -> 데이터가 너무 많을때 발생하는 문제
# 데이터 줄여야함
# 1. 특성들 중에서 상관관계가 가장 낮은것부터 삭제(drop)
# 2. 전처리가 필요한 상황인데 전처리할때 많은 시간을 소요할수 없음
# -상관관계가 높은 컬럼부터 전처리를 진행하는게 효율적.

# 데이터 스케일링
# 주의사항 : 데이터 전처리 가장 마지막에 사용
# 결측치가 없는 상태에서 사용 
# 이상치는 있어도됌.

#%%
from sklearn.preprocessing import StandardScaler
# %% 스케일러 객체 생성
scaler = StandardScaler()
# %% 데이터 프레임과 관련한 통계치 확인
X.describe()
# %% Scaler객체가 데이터의 분포가 어떻게 되어있는지 파악
scaler.fit(X)
# %% 문제 데이터 정규화
X_trans = scaler.transform(X)
# %%
X_trans = pd.DataFrame(X_trans,columns=X.columns)
# %%
X_trans.describe()
# %% 훈련과 평가 데이터 분리
#%%
from sklearn.model_selection import train_test_split
# train : test = 0.75 : 0.25
# 1.train,test 나누는 도구 가져오기
#%%
# 2.도구 활용해서 데이터 분할
# X_trans사용해서 분할하기 ,random_state = 5
# X_train ,y_train ,X_train ,y_test   모양을 출력
X_train, X_test, y_train, y_test = train_test_split(
    X_trans, y, test_size=0.25, random_state=5 
)
#%%
X_train.shape, X_test.shape, y_train.shape, y_test.shape
#%% 모델 선택 및 하이퍼파라미터 튜닝
# 수학적 공식을 이용한 해석적 모델 => LinearRegressor
# 경사하강법 => SGDRegressor
#%%
from sklearn.linear_model import LinearRegression
#%%
from sklearn.linear_model import SGDRegressor
#%%
linear_model = LinearRegression()
#%%
linear_model.fit(X_train,y_train)
# %%
sgd_model=SGDRegressor(eta0=0.000000000001,verbose=2)
#%%
sgd_model.fit(X_train,y_train)
#%% R2 score 0~1 사이의 값을 가진다.
linear_model.score(X_test,y_test)
#%% 음수가 나올수있음.
sgd_model.score(X_test,y_test)
#%% 선형모델의 단점 
#   -모델이 잘못 되었을 경우 수정이 안됌.
#   -규제를 가해서 단점을 해소!
#   -L1규제 + 선형모델 : Lasso
#   -L2규제 + 선형모델 : Ridge
# 규제란? 선형모델 가중치(w)를 영향을 주겠다. => 모델에 개입하겠다.

# %%    *L2규제
#       특성의 중요도를 바탕으로 가중치를 조절
#       중요도가 높은 특성 : 가중치 극대화
#       중요도가 낮은 특성 : 가중치를 0에 가깝게 만듦(0으로 만들지는 않음)
#%%     *L1규제
#       특성의 중요도를 바탕으로 가중치를 조절
#       중요도가 높은 특성 : 가중치 극대화
#       중요도가 낮은 특성 : 가중치를 0으로 만듦 -> 사용하지 않음
#%%     L2규제 사용
from sklearn.linear_model import Ridge
# %% 하이퍼파라미터 : 규제 강도를 조절하는 alpha
# alpha값 증가 -> 규제를 늘리고 -> 모델이 단순해짐 -> 과대적합 해결
# alpha값 감소 -> 규제를 줄이고 -> 모델이 복잡해짐 -> 과소적합 해결

#%%
def ridge_alpha(alpha) :
    ridge = Ridge(alpha=alpha) #모델 생성
    ridge.fit(X_train,y_train) #모델 학습
    print("훈련용 데이터 : ",ridge.score(X_train,y_train))
    print("테스트용 데이터 : ",ridge.score(X_test,y_test))
# %%
