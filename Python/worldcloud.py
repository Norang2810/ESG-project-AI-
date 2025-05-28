#%%

file_path ='KakaoTalk_20250528_1731_41_586_김준수.txt'
f =open(file_path,'rt' ,encoding='UTF8')
lines = f.readlines()
print(lines[5].split(']'))


# %%
nouns = []
for line in lines:
    try:
        noun = line.split(']')[2].strip()
        nouns.append(noun)
    except:
        pass

# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# %%
#워드 클라우드의 속성값 설정
cloud = WordCloud('C:/Windows\Fonts/gulim.ttc', #사용할 폰트
                  background_color='white', # 배경 색
                  max_font_size=200, #사용할 단어의 수
                  margin=1) #단어끼리 간격 값
# %%
# 하나의 문자열에 값 전부 집어넣기

txts = ''
for noun in nouns:
    txts += f' {noun}'
# %%
txts
# %%
# worldcloud 만들기기
make_cloud = cloud.generate_from_text(txts)
plt.figure(figsize= (8,8))#크기 조절
plt.imshow(make_cloud)
# 축값 제거
plt.xticks([])
plt.yticks([])
plt.show()
# %%
# kiwi : korean Intelligent Word Identifier
# 지능형 한국어 형태소 분석기
# 명사만 추출 라이브러리
import sys
!{sys.executable} -m pip install kiwipiepy

from kiwipiepy import Kiwi
kiwi = Kiwi()
result = kiwi.analyze(txts) 
# %% 
# 0: 글자
# 1: 형태소
# 2: 글자가 시작하는 인덱스 번호
# 3: 글자의 길이
result[0][0]
# %%
results = []
for token,pos,_,_ in result[0][0]:
   if pos == 'NNG': 
        results.append(token)
# %%
results

# %%
txts = ''
for result in results:
    txts += f' {result}'
txts
# %%
make_cloud = cloud.generate_from_text(txts)
plt.figure(figsize= (8,8))#크기 조절
plt.imshow(make_cloud)
# 축값 제거
plt.xticks([])
plt.yticks([])
plt.show()
# %%
from PIL import Image #이미지 불러오는 라이블리
mask = Image.new("RGBA",(220,220),(255,255,255))
img = Image.open("워드클라우드모양.png").convert('RGBA') #이미지 열기 /타입변경
x,y = img.size
mask.paste(img,(0,0,x,y),img)
import numpy as np
mask = np.asanyarray(mask)
# %%
cloud = WordCloud('C:/Windows\Fonts/gulim.ttc', #사용할 폰트
                  background_color='white', # 배경 색
                  max_font_size=200, #사용할 단어의 수
                  margin=1 , #단어끼리 간격 값
                  mask = mask #모양 바꾸기
                  ) 
# %%
make_cloud = cloud.generate_from_text(txts)
plt.figure(figsize= (8,8))#크기 조절
plt.imshow(make_cloud)
# 축값 제거
plt.xticks([])
plt.yticks([])
plt.show()
# %%
