# Food_Classification_with_Transfer_Learning
- Food 101 데이터를 통한 전이학습 결과 확인
- ImageNet으로 학습 된 MobileNet 모델 사용


## Experiment environment
- AWS Environment

|분류|유형|비고|
|:----------:|:------------:|:---:|
|  Instance  | g4dn.2xlarge |     |
|    vCPU    |      8       |     |
|   Memory   |    32GiB     |     |
|    GPU     |  NVIDIA T4   |     |
| GPU Memory |    16GiB     |     |


## Result
- OOM으로 인한 실험 실패
- 만족할만한 성능 (90% 이상)으로 학습시키기에는 컴퓨팅 자원이 부족


# FoodClassifier
- GPT-4o 모델을 이용하여 음식 분류


## How to use
1. 환경변수에 'OPENAI_API_KEY'라는 이름으로 OpenAI API Key 등록
2. classify_food 함수를 <이미지 경로> 인자로하여 호출
  ```py
  from FoodClassifier import classify_food

  print(classify_food('<image path>'))
  ```
3. 분류된 음식 종류 한국어로 반환
