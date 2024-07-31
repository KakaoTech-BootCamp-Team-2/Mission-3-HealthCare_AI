import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
exercise_data = pd.read_csv('./exercise_data.csv')

# 그래프 그리기
plt.figure(figsize=(100, 20))  # 그래프 크기 설정
plt.plot(exercise_data['Activity, Exercise or Sport (1 hour)'], exercise_data['Calories per kg'], marker='o', linestyle='-')
plt.title('exercise-calories')  # 그래프 제목
plt.xlabel('exercise')  # x축 라벨
plt.ylabel('calories in kg')  # y축 라벨
plt.grid(True)  # 그리드 표시
plt.xticks(rotation=45)  # x축 라벨 회전
plt.tight_layout()  # 레이아웃 조정
plt.savefig('exercise.png')  # 그래프를 파일로 저장