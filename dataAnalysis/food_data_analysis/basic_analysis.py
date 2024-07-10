import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'  # macOS의 경우 'AppleGothic', Windows의 경우 'Malgun Gothic'

# 데이터 로드
exercise_data = pd.read_excel('./food_data.xlsx') #pd.read_excel xlsx 문서 읽기, pip install openpyxl 필요

# 데이터의 처음 100개의 행만 선택
subset_data = exercise_data.head(100)

# 그래프 그리기
plt.figure(figsize=(40, 20))  # 그래프 크기 설정
plt.plot(subset_data['식품명'], subset_data['에너지(kcal)'], marker='o', linestyle='-', color='pink',linewidth=4)
plt.title('food-calories')  # 그래프 제목
plt.xlabel('food')  # x축 라벨
plt.ylabel('calories')  # y축 라벨
plt.grid(True)  # 그리드 표시
plt.xticks(rotation=45)  # x축 라벨 회전
plt.tight_layout()  # 레이아웃 조정
plt.savefig('food.png')  # 그래프를 파일로 저장