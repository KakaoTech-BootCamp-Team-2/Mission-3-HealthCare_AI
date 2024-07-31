import pandas as pd

# 데이터를 로드
diet_data = pd.read_csv('./diet_data.csv')

# 데이터 형식 확인
#print(diet_data.dtypes)

# 문자 제거 및 수치형 데이터로 변환
diet_data['cals_per_oz'] = pd.to_numeric(diet_data['cals_per_oz'], errors='coerce')
diet_data['five_donuts'] = pd.to_numeric(diet_data['five_donuts'], errors='coerce')

# 결측값 처리
diet_data['cals_per_oz'] = diet_data['cals_per_oz'].fillna(diet_data['cals_per_oz'].mean())
diet_data['five_donuts'] = diet_data['five_donuts'].fillna(0)

# 통계 확인
print(diet_data.describe())

