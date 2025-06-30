#%% (인공지능 7과정 1.문제정의)
# 1.붓꽃 꽃잎의 길이,너비 / 꽃받침의 길이 ,너비 특징 4개를 활용해서 붓꽃의 품종('setosa','versicolor','virginica')을 예측
# 2.hyperparameter 조정
# %% 환경세팅
# 1.numpy -> np
# 2.pandas -> pd
# 3.matplotlib -> plt

# %% -->데이터분석에 필요한 도구
import numpy as np
# %%
import matplotlib.pyplot as plt
# %%
import pandas as pd
# %%
from sklearn.neighbors import KNeighborsClassifier
# %%
from sklearn.metrics import accuracy_score
# %%
from sklearn.model_selection import train_test_split
# %%  데이터 불러오기
from sklearn.datasets import load_iris
# %%
load_iris()
# %% 딕셔너리 형식으로 데이터가 담김
# 사이킷런(sklearn)에서 제공하는 번치(bunch)객체
iris_data = load_iris()
# %%
iris_data.keys()
# %%
X = iris_data['data']
# %% -모양
X.shape
# %% - data type
X.dtype
# %% - 차원-> n-dimension
X.ndim
# %% 항상 데이터분석할때는 데이터의 특성을 파악하는 습관!
X[:5]  # 처음 5개 행만 출력
# %%
iris_data['feature_names']  # feature_names
# %%
# ['sepal length (cm)', :꽃받침 길이
#  'sepal width (cm)',  :꽃받침 너비
#  'petal length (cm)', :꽃잎 길이
#  'petal width (cm)']  :꽃잎 너비
# %% 정답 데이터 살펴보기
iris_data['target']
# 'setosa' : 0 ,'versicolor' : 1 , 'virginica' : 2
# 3가지의 품종을 문자열로 표현할 경우 컴퓨터가 알아들을수 없기 때문에
# 숫자로 매핑 시켜준것!
# %%
iris_data['target_names']

# %% 데이터 셋 구성
# -특정 데이터 (X,Feature)만 DataFrame으로 변경
# train_test_split도구를 활용해서 train,test,set을 분리
#%% X-array를 DataFrame으로 변경
dic = {iris_data['feature_names'][0] : X[:, 0],
        iris_data['feature_names'][1] : X[:, 1],
        iris_data['feature_names'][2] : X[:, 2],
        iris_data['feature_names'][3] : X[:, 3]}
# dic
iris_df = pd.DataFrame(X,columns=iris_data.feature_names)  # DataFrame으로 변경   
# iris_data['feature_names']
# %% Feature (X) / Target (y) 정의
X = iris_data['data']  # 꽃받침/꽃잎 길이 너비 등 4가지 특성
y = iris_data['target']  # 정답: 품종 레이블 (0, 1, 2)

# %% train-test 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # test는 20%, 랜덤시드 고정
)

# %% KNN 모델 정의
knn = KNeighborsClassifier(n_neighbors=3)  # 하이퍼파라미터: 이웃 개수 K=3

# %% 모델 학습
knn.fit(X_train, y_train)

# %% 예측 수행
y_pred = knn.predict(X_test)

# %% 정확도 평가
acc = accuracy_score(y_test, y_pred)
print(f"정확도: {acc:.2f}")  # 소수점 둘째 자리까지

# %% 예측 결과 일부 확인
print("예측값:", y_pred[:10])
print("실제값:", y_test[:10])


# %%