"""
실습목표
1.버섯의 특징을 활용해 독/식용 버섯을 분류하는 실습
2.Decision Tree 분류 모델을 학습시키고 시각화 & 과대적합 제어를 수행하자
모델 자체적으로 특성 중요도 선택한 것을 확인해보기
"""

# %%
import pandas as pd

# %%
import numpy as np

# %%
import matplotlib.pyplot as plt

# %% 데이터 불러오기!
# pandas 에서 제공하는 read_csv함수를 사용해서 csv파일을 불러오기
data = pd.read_csv("./data/mushroom.csv")  ## data변수에 저장
# %% 데이터 확인! .info() => 컬럼이름, 행열 크기, 결측치 여부, 데이터 타입
data.info
# %%
data.isnull().sum()
# %%
X = data.drop(columns=["poisonous"])
# %%
y = data["poisonous"]
# %%
print("문제 데이터 크기 :", X.shape)
print("문제 데이터 크기 :", y.shape)
# %% 정답 데이터 살펴보기
# 독성, 식용 각각 몇개씩 들어있는지 확인!
y.value_counts()

# %% 문자형 데이터 -> 수치(숫자로) 변환
"""     
        1.레이블 인코딩 :클래스이름 ->  숫자로 매칭
        -혈액형
        A : 0 , B : 1,  AB : 2, O : 3
        클래스 간에 대소관계가 생김
        ex) 회사 직원들의 연봉 예측
        직급 :        사원 : 3, 책 : 1, 사장 : 2 <-잘못 해석될 가능성이 존재
        순서가 무관한 모델에 많이 사용
        
        
         
        2.원핫 인코딩 : 각 클래스 이름에 해당하는 컬럼을 만들고 True/False로 해당하는 클래스 표시
        A | B | AB | O
        1 | 0 | 0  | 0
"""
from sklearn.preprocessing import LabelEncoder
# %% 인코딩은 데이터 전처리 과정의 일부
X_label = X.copy()  # 원본 데이터 보존을 위해 복사

# %% 인코더 객체 생성
encoder = LabelEncoder()
# %% 
encoder.fit(X_label['cap-shape']) # 컬럼을 어떻게 인코딩할지 파악하는 과정
X_label['cap-shape'] = encoder.transform(X_label['cap-shape'])  # 인코딩 수행
# %% 
result = X_label['cap-shape'].unique()# 인코딩된 값 확인
result.sort()
# %%
print(result)
# %% pd.get_dummies()를 사용한 원핫 인코딩
X_oh = pd.get_dummies(X)
# %%
X_oh.shape
# %% train,test 데이터 분리
"""
    1.sklearn.model_selection.train_test_split() 함수를 사용해서
    2.데이터를 학습용(train)과 테스트용(test)으로 7:3 비율로 분리합니다.
    - X_train, X_test, y_train, y_test 에 저장
    3. 잘 분리되었는지 X_train, X_test, y_train, y_test 의 크기를 출력합니다.
"""
# %%
from sklearn.model_selection import train_test_split
# %%
X_train, X_test, y_train, y_test = train_test_split(X_oh, y, test_size=0.3, random_state=3)
# %%
X_train.shape, X_test.shape, y_train.shape, y_test.shape
# %%
from sklearn.tree import DecisionTreeClassifier
# %%
tree_model = DecisionTreeClassifier()
# %% 트리모델이 가지를 뻗어나갈 수 있을 만큼 최대로 뻗어 나감
#  과대 적합의 가능성이 있음
tree_model.fit(X_train, y_train)
# %%
tree_model.predict(X_test)  # 예측 수행
# %%
from sklearn.metrics import accuracy_score
# %%
y_pred = tree_model.predict(X_test)  # 예측값
# %%
accuracy = accuracy_score(y_test, y_pred)  # 정확도 계산
# %%
print("정확도:", accuracy)  # 정확도 출력
# %%
from sklearn.model_selection import cross_val_score
# %%
cross_val_scores = cross_val_score(tree_model, X_train, y_train, cv=5)  # 5겹 교차 검증
# %%
print("교차 검증 정확도:", cross_val_scores)  # 교차 검증 정확도 출력
# %%
print("평균 교차 검증 정확도:", np.mean(cross_val_scores))  # 평균 교차 검증 정확도 출력
# %% array형태로 각 컬럼들이 독버섯을 분류하는데 얼마나 중요한지 수치로 확인
tree_model.feature_importances_

# %% df로 변환
fi_df = pd.DataFrame(tree_model.feature_importances_,              index=X_oh.columns,
              columns=["importance"])
# %%
fi_df['importance'].sort_values(ascending=False) # 냄새가 안나는 : odor_n 칼럼이 분류에 가장 큰역할을 함!

# %%
from sklearn.tree import export_graphviz
# %%
export_graphviz(tree_model, out_file="./data/tree.dot", 
                class_names=["식용", "독성"],
                feature_names=X_oh.columns,
                impurity=True,
                filled=True,
                )

# %%
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
#%%
# 트리 시각화 (크게 보기 위해 figsize 지정)
plt.figure(figsize=(20, 10))  # (가로, 세로)
plt.rcParams['font.family'] = 'Gulim'  # 한글 폰트 설정 (Gulim은 Windows에서 기본 제공되는 한글 폰트 중 하나입니다)
# 트리 그리기
plot_tree(tree_model,
          feature_names=X_oh.columns,
          class_names=["식용", "독성"],
          filled=True,
          impurity=True,
          rounded=True,
          fontsize=8)

plt.title("의사결정나무 시각화")
plt.show()

# %%
