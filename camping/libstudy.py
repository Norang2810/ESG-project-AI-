
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

# 시각화 폰트설정
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)  # 음수 부호 깨짐 방지

data = pd.read_csv('C:\Dev\ESG\camping\Con04_전국야영(캠핑)장표준데이터.csv',encoding='euc-kr')  # 한글 깨짐 방지

data.head()  # 데이터의 처음 5행을 출력합니다.

data.shape  # 데이터의 행과 열의 개수를 출력합니다.

data.info()  # 데이터의 정보(열의 개수, 데이터 타입 등)를 출력합니다


data.isnull().sum()  # 각 열의 결측치 개수를 출력합니다.

# Misiingno 이용하여 결측치 보기
import missingno

missingno.matrix(data)

missingno.bar(data)

# 전체 컬럼 출력    
pd.set_option('display.max_columns', None)  # 모든 열을 출력하도록 설정

data.head(1)  # 데이터의 처음 5행을 출력합니다.

data.columns  # 데이터의 열 이름을 출력합니다.

data.isnull().sum()  # 각 열의 결측치 개수를 출력합니다.
#%%
data.isnull().sum() == data.shape[0]  # 각 열의 결측치 개수를 데이터의 행 개수로 나누어 비율을 계산합니다.

null_data = data.columns[data.isnull().sum() == data.shape[0]]

len(null_data)

data.drop(null_data, axis=1,inplace=True)  # 결측치가 있는 열을 삭제합니다.

data.columns

data.shape

data.isnull().sum().sort_values(ascending=False)  # 결측치가 있는 열을 내림차순으로 정렬하여 출력합니다.

data.isnull().sum().sort_values(ascending=False).head(6)  # 결측치가 있는 상위 10개 열을 출력합니다.

null_data=data.isnull().sum().sort_values(ascending=False).head(6).index  # 결측치가 있는 상위 6개 열의 이름을 출력합니다.
null_data  # 결측치가 있는 상위 6개 열의 이름을 출력합니다.

data.drop(null_data, axis=1, inplace=True)  # 결측치가 있는 상위 6개 열을 삭제합니다.

data.head()  # 데이터의 처음 5행을 출력합니다.

len(null_data)

data.shape

data.isnull().sum().sort_values(ascending=False)  # 결측치가 있는 열을 내림차순으로 정렬하여 출력합니다.

data['소재지도로명주소'].isnull()

data[data['소재지도로명주소'].isnull()]

data['소재지지번주소'].isnull()

data[data['소재지지번주소'].isnull()]

data [(data['소재지지번주소'].isnull()) & (data['소재지도로명주소'].isnull())]

# '소재지도로명주소'의 결측치 데이터 확인
data.loc[data['소재지도로명주소'].isnull(),'소재지도로명주소']

len(data.loc[data['소재지도로명주소'].isnull(),'소재지도로명주소'])


data.loc[data['소재지도로명주소'].isnull(),'소재도로명주소']

len(data.loc[data['소재지도로명주소'].isnull(),'소재지지번주소'])

# '소재지도로명주소' 의 결측치를 '소재지지번주소' 값으로 채우기
data.loc[data['소재지도로명주소'].isnull(), '소재지도로명주소'] = \
    data.loc[data['소재지도로명주소'].isnull(), '소재지지번주소']

print(data['소재지도로명주소'].isnull().sum())

data[['소재지도로명주소', '소재지지번주소']]

# 소재지지번주소 컬럼삭제
del data['소재지지번주소']

data.head()

data.info()

data['제공기관코드'].unique()

del data['제공기관코드']

del data['소재도로명주소']

data.shape

data.head()

data.shape

data['소재지도로명주소']

data['소재지도로명주소'].str.split(' ')

for i in range(len(data)):
    print(data.loc[i,'소재지도로명주소'].split(' ')[0])
    # print(data.loc[i,'소재지도로명주소'])

for i in range(len(data)):
    data.loc[i,'시도명'] = data.loc[i,'소재지도로명주소'].split(' ')[0]

data

data[['소재지도로명주소','시도명']]

# 시군구명 컬럼 생성

data['소재지도로명주소'].str.split()

data['소재지도로명주소'].str.split(expand=True) #리스트 -> 데이터프레임 형태로 변함.

data['소재지도로명주소'].str.split(expand=True)[0]

data['소재지도로명주소'].str.split(expand=True)[1]

data['시군구명'] = data['소재지도로명주소'].str.split(expand=True)[1]

data

data[['소재지도로명주소','시군구명']]


data['시도명'].unique()

#시도명 컬럼 빈도수 보기
data['시도명'].value_counts()

# 위도 경도 이용해 산점도 표시

data

plt.figure(figsize=(5,7))
sns.scatterplot(data=data, x='경도' , y ='위도')
 
# '시도명' 별로 구분짓기
plt.figure(figsize=(5,7))
sns.scatterplot(data=data, x='경도' , y ='위도',hue='시도명')

plt.figure(figsize=(5,7))
sns.scatterplot(data=data, x='경도' , y ='위도',hue='시도명')
plt.legend(bbox_to_anchor=(1.2,1))
 
# 수치 데이터 시각화
data['야영사이트수']

data['야영사이트수'].plot.hist()
 
# '야영사이트수' 가 100개 이하인 데이터 시각화
data [ data['야영사이트수'] <= 100 ] ['야영사이트수'].plot.hist()

data[data['야영사이트수'] >= 100]['야영사이트수'].plot.hist()
 
# Seaborn 라이브러리 이용하기
sns.histplot(data = data , x='야영사이트수')

sns.distplot(data['야영사이트수'])

sns.distplot(data[data['야영사이트수'] <= 100]['야영사이트수'])
 
# '야영사이트수'가 100개 이상인 데이터 Seabron 라이브러리 이용하기
sns.distplot(data[data['야영사이트수'] >= 100]['야영사이트수'])

 
# cut함수 이용하여 범주데이터로 바꾸기
# 수치데이터 범주데이터로 바꾸기
bins = [-1,20,45,85,130,500]
labels = ['a','b','c','d','e']

pd.cut(data['야영사이트수'],bins = bins , labels = labels).value_counts().plot.bar()

# 캠핌장 편의시설 파악하기

data['편의시설']

f_list = []
for fac in data['편의시설'] :
    f_list.append(fac)

f_list

ex_list = ['list','를','문자열','로','바꾸기']
ex_list

# 리스트를 문자열로 변환하기 -> join 
' '.join(ex_list)     # join함수 유용함

f_list

# 리스트에 담긴 문자열로 바꾸기
f_str = ','.join(f_list)
f_str

data['편의시설'].unique()

# '+'문자열을 ','로 바꾸기
f_str.replace('+',',')

# '+' , '-','/' 문자열을 ','로 바꾸기
f_str = f_str.replace('+',',').replace('/',',').replace('+',',')

f_str

# 정규표현식 이용하기 (텍스트 처리)
# re 라이브러리 import 
import re


# 정규표현식 이용하여 빈칸 없애기

re.sub('[\s]','',f_str)

# 숫자 없애기 
re.sub('[\d]','',f_str)

re.sub('[\s\d동]','',f_str)
def remove_digits(text):
    if pd.isnull(text):  # 결측치 처리
        return text
    return re.sub('\d+', '', text)

# 두개의 ,를 하나의 ,로 바꿔줌
re.sub(',{2,}','',f_str)

f_str.split(',')

pd.Series(f_str.split(','))

# series 데이터여서 value_counts가능
f_cnt = pd.Series(f_str.split(',')).value_counts()
f_cnt

pd.Series(f_str.split(',')).unique()

f_cnt.head(30)

f_cnt.tail(30)

f_str.count('.')

# .이 들어간 문자열의 첫번째 위치
f_str.find('.')

f_str[12090-3 : 12090+4]

# '.'이 들어간 문자열 출력하기
for fac in f_str.split(','):
    if '.' in fac:
        print(fac)

# '.' 문자열을 ',' 로 바꾸기
f_str = f_str.replace('.',',')
f_str

# 찿는 문자열이 없으면 -1값
f_str.find('.')

f_cnt = pd.Series(f_str.split(',')).value_counts()

f_cnt.head(30).plot.bar()

# 워드클라우드 라이브러리 (중요도,인기도 고려)
from wordcloud import WordCloud


wc = WordCloud(font_path='C:\\Windows\\Fonts\\malgun.ttf',
                width = 1200,
                height= 500,
                background_color='white',
                random_state=3
                )

wc.generate(f_str)
plt.figure(figsize=(15,10))
plt.imshow(wc)
plt.show()
g
