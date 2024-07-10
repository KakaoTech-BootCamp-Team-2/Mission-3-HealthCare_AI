import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn 라이브러리를 사용하여 시각화를 더욱 향상

# 데이터 로드
diet_data = pd.read_csv('./diet_data.csv')

# 필요한 컬럼만 선택하고 결측치 제거
filtered_data = diet_data[['weight_oz', 'calories']].dropna()

# 상관 계수 계산
correlation_matrix = filtered_data.corr()

# 상관 계수 출력
print("Correlation Matrix:")
print(correlation_matrix)

# 상관 관계 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Analysis between Weight and Calories')
plt.savefig('Correlation.png')
