# %% DF생성을 위한 라이브러리
import pandas as pd

# %% DF생성을 위한 라이브러리
import numpy as np

# %% DF생성을 위한 라이브러리
import matplotlib.pyplot as plt

#  성적 데이터를 담은 DF생성
# index지정['은유', '자영', '지희', '영화']
# columns지정['시간', '성적']
# data 변수에 저장
#%%
data = pd.DataFrame(
    [[2, 20], [4, 40], [8, 80], [9, 90]],
    index=["은유", "자영", "지희", "영화"],
    columns=["시간", "성적"],
)
#%%
"""
        MSE가 최소가 되는 최적의 w,b를 찾는 법
        MSE(Mean Squared Erroer, 평균제곱오차) ->비용함수(cost)
    1.수학 공식을 통해서 한번에 최적의 w,b를 구하는 방법
    2.경사하강법(Gradient Descent)이라는 방법을 통해서 반복적으로 최적의 w,b를 구하는 방법
"""
# 수학 공식을 통해서 한번에 최적의 w,b를 구하는 방법
# Linear Regression(선형회귀) 모델을 사용
#%%
from sklearn.linear_model import LinearRegression
# %%
linear_model = LinearRegression()  # LinearRegression 모델을 불러옴
# %% 모델학습(fit)
linear_model.fit(data[["시간"]], data["성적"])  # 문제 : 시간열을 X로, 정답 : 성적열을 y로 지정하여 모델 학습
# 모델 학습을 시킬때 문제 데이터는 2차원 배열로, 정답 데이터는 1차원 배열로 지정해야함
# 시간이라는 컬럼 한개만 넘겨주지만 DataFrame형태로 넘겨줘야함
# linear_model을 fit해주면 수식을 통해 최적의 w,b를 찾아줌
# %% 선형 모델의 기본식
# y = wx + b
# Linear_model 객체를 통해서 w와 b를 확인할 수 있음
print(f'가중치 : {linear_model.coef_}')  # w # 가중치
#%% 절편
print(f'절편 : {linear_model.intercept_}')  # b # 절편

# %% 7시간 공부했을때 몇점인지 예측
linear_model.predict([[7]])  # 7시간 공부했을때 몇점인지 예측(문제데이터 이므로 2차원배열형태)
# 수학적 공식을 이용한 해석적 모델(Analytical Model)
# -모델이 가정한 공식이 완벽하지 않으면 , 예측이 부정확
# -수식 기반이기 때문에 공식이 잘못되면 수정이 어렵고 유연성이 떨어짐
#%%  H(x) = wx + b
def h(w,x):
    return w * x + 0
# %%비용함수 (cost function)
# -모든 데이터의 손실(Lose)값의 합 : 비용
# -오차(Error)값의 제곱 : 손실
# -(예측값 - 실제값) : 오차
# %%
def cost(data,target,weight) : #data문제 , target정답, weight가중치
    y_pred = h(weight, data)  # 예측값
    mse = ((y_pred - target) ** 2).mean() # MSE 계산
    return float(mse)
# %%
# 비용함수(cost function) 테스트
cost(data['시간'],data["성적"],5)  # 가중치 5일때 비용함수 계산
# %%
cost(data['시간'],data["성적"],8) # 가중치 8일때 비용함수 계산
# %%
cost(data['시간'],data["성적"],10) # 가중치 10일때 비용함수 계산
# %% 가중치 변화에 따른 비용함수의 변화를 그래프로 시각화
cost_list = []  # 비용함수 값을 저장할 리스트
# 가중치 1~19 1씩 증가시키면서 비용함수 계산
for w in range(1, 20):
    err = cost(data["시간"],data["성적"],w)
    cost_list.append(err)  # 비용함수 값을 리스트에 추가
    
cost_list       
# %%
plt.plot(range(1, 20), cost_list)  # 가중치 1~19에 대한 비용함수 그래프
plt.xlabel("가중치(w)")  # x축 레이블
plt.ylabel("비용함수(MSE)")  # y축 레이블
plt.title("가중치 변화에 따른 비용함수 변화")  # 그래프 제목
plt.show()  # 그래프 출력
# %% 모델 채점 하기
linear_model.score(data[["시간"]], data["성적"])  # 모델의 채점 점수
# 회귀 모델에서 score() 함수는 결정계수(R^2)를 반환
# 결정계수(R^2)는 모델이 데이터를 얼마나 잘 설명하는지를 나타내는 지표
# 1에 가까울수록 모델이 데이터를 잘 설명함을 의미

# %% 경사하강법(Gradient Descent)이라는 방법을 통해서 반복적으로 최적의 w,b를 구하는 방법
# 경사하강법(Gradient Descent) 구현
#%%
from sklearn.linear_model import SGDRegressor
# %% 모델 생성 및 하이퍼파라미터 설정
sgd_model= SGDRegressor(max_iter=500,
             eta0=0.001, #학습률(learning rate)
             verbose=1) #학습과정을 확인 
# %%
sgd_model.fit(data[["시간"]], data["성적"])  # 모델 학습
# %% 예측
sgd_model.predict([[7]])  # 7시간 공부했을때 몇점인지 예측
# %% 가중치,편향 출력하기
print(f'가중치 : {sgd_model.coef_}')  # w  가중치
print(f'편향 : {sgd_model.intercept_}')  # b  절
# %% score() 함수로 모델 채점하기
sgd_model.score(data[["시간"]], data["성적"])  # 모델의 채점 점수
# %%
# 경사하강법(Gradient Descent)으로 비용함수 변화 시각화
cost_list = []  # 비용함수 값을 저장할 리스트
# 가중치 1~19 1씩 증가시키면서 비용함수 계산
for w in range(1, 20):
    err = cost(data["시간"], data["성적"], w)
    cost_list.append(err)  # 비용함수 값을 리스트에 추가
cost_list

# %%
plt.plot(range(1, 20), cost_list)  # 가중치 1~19에 대한 비용함수 그래프
plt.xlabel("가중치(w)")  # x축 레이블
plt.ylabel("비용함수(MSE)")  # y축 레이블
plt.title("가중치 변화에 따른 비용함수 변화")  # 그래프 제목
plt.show()  # 그래프 출력
# %%
