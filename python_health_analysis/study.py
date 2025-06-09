#%%
import pandas as pd
# %%
import numpy as np
# %%
import matplotlib.pyplot as plt
# %%
import seaborn as sns
# %%
plt.rc('font', family = 'Malgun Gothic')
# %%
data = pd.read_csv('C:\\Dev\\ESG\\python_health_analysis\\Con03_소상공인시장진흥공단_상가업소정보_의료기관_201909.csv',encoding='cp949') #cp949, euc-kr <= encoding
# %%
data.head(5)
# %%
data.columns
# %%
data.shape
# %%
# 데이터 정보보기 (간략하게)
data.info()
# %%
# 결측치 판단 함수
data.isnull().sum() 
#True == 1
#False == 0
# %%
data.isnull().sum().plot.bar(figsize = (15,10))
# %%
plt.figure(figsize = ( 10,10))
sns.heatmap(data.isnull()) # seaborn 라이브러리 이용하여 heatmap 그리기

# %%
# Missingo 라이브러리 import
import missingno as msno

# %%
# missingo 라이브러리 매트릭스 함수
msno.matrix(data) #씨본의 히트맵과 유사 
# %%
msno.bar(data)
#%%
# 결측치가 많은 컬럼 제거하기

data.isnull().sum().sort_values(ascending=False)
# %%
# 결측치 갯수가 많은 9개 데이터 가져오기
null_data = data.isnull().sum().sort_values().tail(9)
# %%
null_data
# %%
# 결측치가 많은 데이터의 컬럼명 추출
null_data.index
# %%
# 결측치가 많은 컬럼 제거하기
data.drop(null_data.index,axis=1,inplace=True)
# %%
pd.set_option('display.max_columns',39)
# %%
data
# %%
data.shape
# %%
data.head(1)
# %%
# 컬러명에 '번호' 문자가 들어간 컬럼 확인
# boolean인덱싱은 True 값만 반환
# data[ 번호문자가 들어간 컬럼 코드 ]
data.columns [data.columns.str.contains('번호')]
# %%
# 컬럼명에 '코드' 문자가 들어간 컬럼 확인
data.columns [data.columns.str.contains('코드')]
# %%
# '코드'문자가 들어간 칼럼의 갯수
data.columns [data.columns.str.contains('코드')].shape  
# %%
# '번호','코드' 들어간 문자 들어간 컬럼 확인
# -> Shift + \ 누르면 | 됌.
data.columns[data.columns.str.contains('번호|코드')]
# %%
# 데이터의 길이 확인법 : shape함수
data.columns[data.columns.str.contains('번호|코드')].shape
# %%
# 데이터의 길이 확인법 : len함수
len(data.columns[data.columns.str.contains('번호|코드')])
# %%
# 변수에 담기 

num_code = data.columns[data.columns.str.contains('번호|코드')]
# %%
num_code
# %%
data.drop(num_code,axis=1,inplace=True)
# %%
data.shape
# %%
# '상권업종대분류명' 칼럼 보기
data['상권업종대분류명'].unique()
# %%
# '대지구분명' 칼럼보기
data['대지구분명'].unique()
# %%
# 사용하지 않을 컬럼 변수에 담기
drop_col = ['상권업종대분류명','대지구분명','행정동명','지번본번지','지번주소','건물본번지']
# %%
# 사용하지않을 컬럼 삭제하기
data.drop(drop_col,axis=1,inplace=True,errors='ignore')
# %%
data.shape
# %%
data.head()
# %%
# 시도별로 살펴보기
# '시도명' 컬럼의 빈도수
data['시도명'].value_counts()
# %%
# '시도명' 칼럼의 빈도수시각화
data['시도명'].value_counts().plot.bar()
# %%
# 경기도 와 서울특별시 와 인천광역시에 위치 -> 수도권
capital = data[(data['시도명'] == '경기도') | (data['시도명'] == '서울특별시') | (data['시도명'] == '인천광역시')] 
# %%
capital
# %%
# 수도권 의료기관 갯수
capital.shape
# %%
# '시도명' bar차트 1
capital['시도명'].value_counts().plot.bar()
# %%
# '시도명 pie chart  (데이터의 점유율 시각화 유용)
capital['시도명'].value_counts().plot.pie()
# %%
# 퍼센트 숫자 시각화
capital['시도명'].value_counts().plot.pie(autopct='%2.f%%' , fontsize=13)
# %%
# 수도권에 포함되지않는 지역 -> 지방권
local = data[(data['시도명'] != '경기도') & (data['시도명'] != '서울특별시') & (data['시도명'] != '인천광역시')] 

# %%
local.head(5)
# %%
local.shape
# %%
# 지방권지역 '시도명' bar chart1
local['시도명'].value_counts().plot.bar()
# %%
# 지방권지역 '시도명' pie chart
local['시도명'].value_counts(ascending=False).plot.pie(autopct='%2.f%%' , fontsize = 10)
# %%
# 업종 분류별로 살펴보기
data.head()
# %%
data['상권업종중분류명'].unique()
# %%
data['상권업종중분류명'].value_counts()
# %%
data['상권업종중분류명'].value_counts().plot.bar()
# %%
# 백분율 비율이 다름름
data['상권업종중분류명'].value_counts(normalize=True).plot.bar()
# %%
count = data['상권업종중분류명'].value_counts()
# %%
count
# %%
labels = data['상권업종중분류명'].value_counts().index
# %%
labels
# %%
# pandas 라이브러리의 내장된 plot차트는 속도빠름 간편함
# matplotlib 라이브러리의 차트는 시각화에 특화됌
plt.pie(count,labels=labels)
# %%
plt.show()
# %%

# %%
