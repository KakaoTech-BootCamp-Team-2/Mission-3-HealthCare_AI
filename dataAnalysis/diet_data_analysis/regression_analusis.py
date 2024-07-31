import pandas as pd
import statsmodels.api as sm

# 데이터 로드
diet_data = pd.read_csv('./diet_data.csv')

# 결측치 제거
filtered_data = diet_data[['weight_oz', 'calories']].dropna()

# 독립 변수에 상수항 추가 (절편)
X = sm.add_constant(filtered_data['calories'])  # 독립 변수
y = filtered_data['weight_oz']  # 종속 변수

# OLS 회귀 모델 구축
model = sm.OLS(y, X)
results = model.fit()

# 결과 출력
print(results.summary())
