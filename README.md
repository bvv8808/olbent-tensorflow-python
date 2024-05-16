### 사용법 안내

**setData.py**  
예측모델을 학습시키고 예측을 진행하기 위한 데이터를 저장하는 프로그램이며, 그 과정에서 아이템 전체의 ID를 DB를 통해 불러옵니다.  
따라서 상품이 `추가` 된다면, `setData.py`를 한 번 실행해 주세요.  
스크립트 실행 예시)) `python setData.py`

**makePrediction.py**

- 저장된 데이터를 통해 예측모델을 새로 훈련 시키고
- 각 성별, 나이, 아이템을 조합하여 나올 수 있는 모든 경우에 대한 구매확률을 예측하고
- 예측된 결과를 DB에 저장합니다
- DB에 저장하기 전에 필터링을 진행하는데 필터 방식은 프로그램 실행 시 매개변수로 입력할 수 있습니다
  - `item`: 각 아이템마다 상위 10개씩만 취합니다
  - `user`(_default_): 각 연령+성별마다 상위 10개씩만 취합니다
  - `top` : 확률이 20%이하인 예측결과를 제합니다
  - `매개변수 미입력 시, 또는 잘못된 매개변수 입력 시`: 각 연령+성별마다 상위 10개씩만 취합니다
  - 스크립트 실행 예시)) `python makePrediction.py item`, `python makePrediction.py user`, `python makePrediction.py top`, `python makePrediction.py top`
