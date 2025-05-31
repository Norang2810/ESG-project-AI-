#%%
f = open ('test.txt'    , 'w')
data = 'Hello, World!\nThis is a test file.\n'
f.write(data)
f.close()

# %%
print(data)
# %%
# get 함수 (txt로 파일로 불러온 홈페이지 소스 데이터 가져옴)
# BS4모듈 : HTML태그를 기반으로 파싱해서 쉽게 검색,분석 가능
# Selenuim 모듈 : 웹 브라우저를 자동으로 제어할 수 있는 모듈
# requests 모듈 : HTTP 요청을 보내고 응답을 받을 수 있는 모듈
# API(Application Programming Interface) : 웹 서비스와 상호작용하기 위한 인터페이스
#%%
# Mathplotlib 모듈 : 데이터 시각화를 위한 라이브러리 (한글 미지원원)
# Seaborn 모듈 : 통계적 데이터 시각화를 위한 라이브러리 (matplotlib 기반) (Statsmodels 패키지에 통계 기능 의지)
# Plotly 모듈 : 대화형 데이터 시각화를 위한 라이브러리 (웹 기반 애플리케이션 Dash에 올려 활용 가능 , 인터렉티브)

# %%
# add_subplot(행, 열, 위치)
# - 행과 열을 나누고 위치를 지정하여 서브플롯을 생성
import matplotlib.pyplot as plt
import numpy as np
# %%
# scatter plot : 산점도 그래프
# twinx() : 두 개의 y축을 가진 그래프를 그릴 때 사용
# twinx()를 사용하면 x축은 동일하게 유지하면서 y축을 두 개로 나눌 수 있음
# twiny() : 두 개의 x축을 가진 그래프를 그릴 때 사용
# twinx()와 twiny()는 각각 y축과 x축을 공유하는 서브플롯을 생성
# plt.subplots() : 서브플롯을 생성하는 함수
# plt.subplots()는 행과 열의 개수를 지정하여 서브플롯을 생성
# plt.subplots()는 서브플롯의 크기와 간격을 조정할 수 있는 다양한 매개변수를 제공
# Matplotlib의 한글 지원을 위해 폰트 설정
# font_manager : Matplotlib에서 폰트를 관리하는 모듈
# savefig() : 그래프를 이미지 파일로 저장하는 함수

