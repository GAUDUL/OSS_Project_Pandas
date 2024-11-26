import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

file_path1='./data/Diseases_Symptoms.csv'
file_path2='./data/Medicine_Details.csv'
file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

dis_df=pd.read_csv(file_path1) #질병 데이터셋
medi_df=pd.read_csv(file_path2) #약 데이터셋
patients_df = pd.read_csv(file_path3) #환자 데이터셋 (증상: cough, fever, fatigue, difficulty breathing)

#Age구간 나누기
bins = [10, 19, 29, 39, 49, 59, 69, 79, 89, 99]  # 구간 정의
labels = ['10~19', '20~29', '30~39', '40~49', '50~59', '60~69', '70~79', '80~89', '90~99']  # 구간 레이블
patients_df['Age'] = pd.cut(patients_df['Age'], bins=bins, labels=labels, right=True)


#문자열로 작성돼있는 값들을 수치화 하기 위한 폼, Low는 1, Normal은 2, High는 3으로 치환
bp_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
chol_mapping = {'Low': 1, 'Normal': 2, 'High': 3}

#Blood Pressure와 Cholesterol Level에 위의 폼 적용
patients_df['Blood Pressure'] = patients_df['Blood Pressure'].map(bp_mapping)
patients_df['Cholesterol Level'] = patients_df['Cholesterol Level'].map(chol_mapping)

#각 나이대별로 혈압과 콜레스테롤 평균 계산
age_group_avg = patients_df.groupby('Age', observed=False)[['Blood Pressure', 'Cholesterol Level']].mean().reset_index()

#그래프 그리기
plt.figure(figsize=(10, 6))

#Blood Pressure와 Cholesterol Level 그래프
sns.lineplot(data=age_group_avg, x='Age', y='Blood Pressure', label='Blood Pressure', marker='o')
sns.lineplot(data=age_group_avg, x='Age', y='Cholesterol Level', label='Cholesterol Level', marker='s')

#그래프
plt.title('Average Blood Pressure and Cholesterol Level by Age')
plt.xlabel('Age')
plt.ylabel('Blood Pressure and Cholesterol Level')
plt.legend()
plt.grid(True)

plt.show()


#선형 회귀 분석

#나이대별 평균 데이터
#나이는 수치형으로 변경
X = age_group_avg['Age'].apply(lambda x: int(x.split('~')[0])).values
y_bp = age_group_avg['Blood Pressure'].values
y_chol = age_group_avg['Cholesterol Level'].values

#독립 변수: Age
#종속 변수: Blood Pressure, Cholesterol Level
X_const = sm.add_constant(X)  # 상수항 추가

# 혈압에 대한 회귀 분석
model_bp = sm.OLS(y_bp, X_const).fit()
# 콜레스테롤 수치에 대한 회귀 분석
model_chol = sm.OLS(y_chol, X_const).fit()

# 회귀 분석 결과 출력
print("Blood Pressure & Age:")
print(model_bp.summary())

print("\nCholesterol Level & Age:")
print(model_chol.summary())