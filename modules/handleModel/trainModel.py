from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split




# 주어진 초기데이터를 바탕으로 모델 생성 및 훈련 후 훈련된 모델을 반환
def train(trainData, labels):

    # 1. 모델 선언 및 정의
    model = keras.Sequential([
        keras.layers.Dense(10, activation='relu'),
        keras.layers.Dense(10, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid'),
    ])

    # 2. 모델 컴파일
    model.compile(optimizer='adam',
                # loss='binary_crossentropy',
                loss='mean_squared_error',
                metrics=['accuracy'])

    # 3. 모델 훈련
    model.fit(trainData, labels, batch_size=3, epochs=5)

    # 4. 훈련이 끝난 모델 반환
    return model
