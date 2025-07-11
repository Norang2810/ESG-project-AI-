# ### 목표 설정
# 1. 앞서 만든 NPZ파일을 불러와서 사용해보자.
# 2. CNN(합성곱 신경망)을 구현해보자.
# 3. 신경망 학습 및 전이학습을 진행해보자.
# 4. Dropout / Early Stopping 사용해보자.**굵은 텍스트**
#%%
# !pip install google google-api-python-client
#%%
# !pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#%% 드라이브 마운트
try:
    from google.colab import drive
    drive.mount('/content/drive')
except ModuleNotFoundError:
    print("Colab 환경이 아님")

#%% 경로 설정
# !cd "C:\\Users\\진우\\Documents\\ESG\\DeepLearning"
#%%
import zipfile
#%%
import os
#%%
zip_path = "cats_and_dogs_filtered.zip"  # 파일이 DeepLearning 폴더 안에 있으니까 상대 경로
#%%
extract_dir = "cats_and_dogs_filtered"   # 압축 해제할 폴더 이름
#%%
# 압축 해제
with zipfile.ZipFile("cats_and_dogs_filtered.zip", 'r') as zip_ref:
    zip_ref.extractall(".")  # 현재 디렉토리에 압축 해제


#%%
print("압축 해제 완료!")

#%%
# !pip install pandas
#%%
# !pip install matplotlib
#%% 필요한 라이브러리 불러오기
import pandas as pd
#%%
import numpy as np
#%%
from matplotlib import pyplot as plt

#%%
# !pip install ipykernel
#%%
# !python -m ipykernel install --user --name=tf310 --display-name "Python (tf310)"

#%%
import sys
print(sys.executable)
#%%
# !pip install tensorflow
#%%
import tensorflow as tf
print(tf.__version__)

#%%

from tensorflow.keras.preprocessing.image import ImageDataGenerator
#%%
train_dir = os.path.join("cats_and_dogs_filtered", "train")
val_dir = os.path.join("cats_and_dogs_filtered", "test")  # vlidation → test
#%%
# 데이터 증강 + 정규화
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
#%%
# 제너레이터 생성
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)
#%%
val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

#%% CNN 신경망 재료 import
from tensorflow.keras import Sequential
#%%
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
#%%
from tensorflow.keras.callbacks import EarlyStopping




#%% 뼈대 설정
cnn_model = Sequential()

#%% 특성 추출부 구현
cnn_model.add(Conv2D(filters= 32,# 필터의 갯수
                     kernel_size = (3,3), # 필터의 크기
                     padding = 'same', # padding 사용 여부 same = 사용/ valid = 미사용
                     activation = 'relu', # 활성화 함수
                     input_shape=(224,224,3) # 이미지 형태
                     ))
cnn_model.add(MaxPooling2D(pool_size= (2,2)))
#%% pool_size : 풀링 영역 지정
#===================================================================================
cnn_model.add(Conv2D(filters= 64,# 필터의 갯수
                     kernel_size = (3,3), # 필터의 크기
                     padding = 'same', # padding 사용 여부 same = 사용/ valid = 미사용
                     activation = 'relu' # 활성화 함수
                     ))
cnn_model.add(MaxPooling2D(pool_size= (2,2)))
#%% pool_size : 풀링 영역 지정
#===================================================================================
cnn_model.add(Conv2D(filters= 128,# 필터의 갯수
                     kernel_size = (3,3), # 필터의 크기
                     padding = 'same', # padding 사용 여부 same = 사용/ valid = 미사용
                     activation = 'relu' # 활성화 함수
                     ))
cnn_model.add(MaxPooling2D(pool_size= (2,2)))

#%% pool_size : 풀링 영역 지정
# 특성 추출부 끝
# 전결합층(분류기 구현)
# 특성추출부와 분류기를 결합하기 위한 Flatten 층 삽입
cnn_model.add(Flatten())
cnn_model.add(Dense(units = 512, activation = 'relu'))
cnn_model.add(Dropout(0.5))
cnn_model.add(Dense(units = 256, activation = 'relu'))
cnn_model.add(Dropout(0.5))

cnn_model.add(Dense(units = 1, activation = 'relu'))

# 신경망 구조 구현 완료



#%% 모델 컴파일
cnn_model.compile(
    loss = 'binary_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy']
)
# #%%
# # 학습 진행 전에 학습 조기중단 설정
# f_early = EarlyStopping(monitor = 'val_accuracy', # 검증 정확도 확인
#                         patience = 5      
#                         )


# #%%
# h_cnn = cnn_model.fit(X_train, y_train,
#                       epochs = 100,
#                       batch_size = 64,
#                       validation_split = 0.2,
#                       callbacks = [f_early] # callback -> 이벤트 부여
#                       )

# 현재 문제는 아담이 학습률이 너무 크게나서 발산 / 학습률 감소 시킨 후 다시 진행
#%%
# !pip install pillow
#%%
# 학습 조기중단 콜백
early_stop = EarlyStopping(
    monitor='val_accuracy',  # 검증 정확도 기준
    patience=5,
    restore_best_weights=True
)
#%%
# 학습
history = cnn_model.fit(
    train_generator,
    epochs=100,
    validation_data=val_generator,
    callbacks=[early_stop]
)





#%%
# 현재 모델의 상태 
# 학습 중간에 표시되는 학습 정확도와 검증 정확도를 확인한 결과 차이가 크다! -> 과대 적합
# Dropout 사용 -> 모델이 너무 복잡해서 학습이 많이 된게 아닐까? -> 일정 뉴런을 비활성화 시켜서 모델의 복잡도를 제어
# EarlyStoping -> 학습이 너무 많이 되서 훈련데이터만 잘 맞추는게 아닐까? -> 학습 조기 중단. 
# 그럼에도 불구하고 성능이 안 좋음(과대적합)
# 이미지를 더 모으거나 이미지 증식을 고려해볼 수 있음
# 이미 학습이 잘된 모델을 가져와서 우리가 사용해 볼수 있음(전이학습)


# %%


from tensorflow.keras.applications import VGG16
#%%
vgg16 = VGG16(weights = 'imagenet', # imagenet 데이터로 학습한 가중치를 사용
              include_top = False, # 분류기는 사용 x
              input_shape =(224,224,3),  #이미지는 모양 (행,열,색상채널)
              )

#특성 추출 방식 구현

# %%
model = Sequential()
#%%
model.add(vgg16)
#%%
model.add(Flatten())
# %% 출력층 구성
model.add(Dense(units=256,activation ='relu'))
model.add(Dense(units=128,activation ='relu'))
model.add(Dense(units=1,activation ='sigmoid'))
# %% 미세조정 방식 구현
# 기존의 특성 추출방식은 특성 추출부와 가중치를 그대로 가져와서 사용
# 내 데이터와 적합한 모델이 아닐수 있기 때문에 특성추추불의 끝부분과 분류기를
# 우리 데이터에 맞는 가중치로 학습시킬 필요가 있음 -> 미세조정 방식
#%%
vgg16 = VGG16(weights = 'imagenet', # imagenet 데이터로 학습한 가중치를 사용
              include_top = False, # 분류기는 사용 x
              input_shape =(224,224,3),  #이미지는 모양 (행,열,색상채널)
              )
# %%
vgg16.summary()
# %% 각층의 이름만 가져와보자
for layer in vgg16.layers :
    print(layer.name)
# %%
# %% 미세 조정방식 구현
model = Sequential()

#%% ==============================================
for layer in vgg16.layers : # vgg16에 모든 층을 돌아보겠다.
    if layer.name == 'block5_conv3' : #층의 이름이 block5_conv3이면
        layer.trainable = True # 해당층이 학습이 가능하도록 만들어주겠다.
    else :
        layer.trainable = False #학습이 되지않도록 가중치를 동결하겠다.
#%% ==============================================
model.add(vgg16)
#%%
model.add(Flatten())
# %% 출력층 구성
model.add(Dense(units=256,activation ='relu'))
model.add(Dense(units=128,activation ='relu'))
model.add(Dense(units=1,activation ='sigmoid'))
# %% 모델 컴파일
model.compile(
    loss = 'binary_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy']
)
# %% 학습
model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator,
    callbacks=[early_stop]  # 조기 종료 콜백이 있다면 추가
)
# %%
