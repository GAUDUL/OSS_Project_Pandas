import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path1='./data/Diseases_Symptoms.csv'
file_path2='./data/Medicine_Details.csv'
file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

dis_df=pd.read_csv(file_path1)
medi_df=pd.read_csv(file_path2)
patients_df = pd.read_csv(file_path3)

# Age구간 나누기
bins = [10, 19, 29, 39, 49, 59, 69, 79, 89, 99]  # 구간 정의
labels = ['10~19', '20~29', '30~39', '40~49', '50~59', '60~69', '70~79', '80~89', '90~99']  # 구간 레이블
patients_df['Age'] = pd.cut(patients_df['Age'], bins=bins, labels=labels, right=True)


#문자열로 작성돼있는 값들을 수치화 하기 위한 폼, Low는 1, Normal은 2, High는 3으로 치환
bp_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
chol_mapping = {'Low': 1, 'Normal': 2, 'High': 3}

#Blood Pressure와 Cholesterol Level에 위의 폼 적용
patients_df['Blood Pressure'] = patients_df['Blood Pressure'].map(bp_mapping)
patients_df['Cholesterol Level'] = patients_df['Cholesterol Level'].map(chol_mapping)

# 각 나이대별로 혈압과 콜레스테롤 평균 계산
age_group_avg = patients_df.groupby('Age', observed=False)[['Blood Pressure', 'Cholesterol Level']].mean().reset_index()

# 선형 그래프 그리기
plt.figure(figsize=(10, 6))

# Blood Pressure와 Cholesterol Level 선형 그래프
sns.lineplot(data=age_group_avg, x='Age', y='Blood Pressure', label='Blood Pressure', marker='o')
sns.lineplot(data=age_group_avg, x='Age', y='Cholesterol Level', label='Cholesterol Level', marker='s')

# 그래프, 나이가 증가할수록 혈압, 콜레스테롤 수치 증가하는 것 확인 가능
plt.title('Average Blood Pressure and Cholesterol Level by Age')
plt.xlabel('Age')
plt.ylabel('Blood Pressure and Cholesterol Level')
plt.legend()
plt.grid(True)

plt.show()