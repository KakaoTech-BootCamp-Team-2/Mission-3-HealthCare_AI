import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
diet_data = pd.read_csv('./diet_data.csv')

# 날짜 데이터를 datetime 형식으로 변환
diet_data['Date'] = pd.to_datetime(diet_data['Date'])

# weight_oz 값이 0이 아닌 데이터만 필터링
filtered_data = diet_data[diet_data['weight_oz'] != 0]

# 체중 데이터 'weight_oz'
# 그래프 그리기
plt.figure(figsize=(10, 5))  # 그래프 크기 설정
plt.plot(filtered_data['Date'], filtered_data['weight_oz'], marker='o', linestyle='-')
plt.title('Time Series of Weight Change')  # 그래프 제목
plt.xlabel('Date')  # x축 라벨
plt.ylabel('Weight in Ounces')  # y축 라벨
plt.grid(True)  # 그리드 표시
plt.xticks(rotation=45)  # x축 라벨 회전
plt.tight_layout()  # 레이아웃 조정
# 그래프 표시 plt.show()는 iterm에서 실행이 안 되나? 무한로딩
plt.savefig('weight_oz.png')  # 그래프를 파일로 저장

# weight_oz 값이 0이 아닌 데이터만 필터링
calorie_filtered = diet_data[diet_data['calories'] != 0]

# 섭취량 데이터 'calories'
plt.figure(figsize=(10, 5))  
plt.plot(calorie_filtered['Date'], calorie_filtered['calories'], marker='o', linestyle='-')
plt.title('Time Series of calories Change')  
plt.xlabel('Date')
plt.ylabel('calories') 
plt.grid(True) 
plt.xticks(rotation=45)
plt.tight_layout() 
plt.savefig('calories.png') 

# 운동량 데이터 'weight_oz'
# walk/run 데이터 이용?

# 겹친 그래프
plt.figure(figsize=(10, 5))  
plt.plot(filtered_data['Date'], filtered_data['weight_oz'], marker='o', linestyle='-', color='blue', label='Weight in Ounces')
plt.plot(calorie_filtered['Date'], calorie_filtered['calories'], marker='x', linestyle='--', color='red', label='Calories')
plt.title('Time Series of Weight and Calorie Changes')  
plt.xlabel('Date')
plt.ylabel('Value') 
plt.grid(True) 
plt.legend() 
plt.xticks(rotation=45)  
plt.tight_layout() 
plt.savefig('combined_changes.png')