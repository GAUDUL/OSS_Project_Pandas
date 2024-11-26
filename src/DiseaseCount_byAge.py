import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path1='./data/Diseases_Symptoms.csv'
file_path2='./data/Medicine_Details.csv'
file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

dis_df=pd.read_csv(file_path1) #질병 데이터셋
medi_df=pd.read_csv(file_path2) #약 데이터셋
patients_df = pd.read_csv(file_path3) #환자 데이터셋 (증상: cough, fever, fatigue, difficulty breathing)

#결과가 Positive인 환자들의 데이터만 가져오기
patients_df = patients_df[patients_df['Outcome Variable'] == 'Positive']

#Age구간 나누기
bins = [10, 19, 29, 39, 49, 59, 69, 79, 89, 99]  # 구간 정의
labels = ['10~19', '20~29', '30~39', '40~49', '50~59', '60~69', '70~79', '80~89', '90~99']  # 구간 레이블
patients_df['Age'] = pd.cut(patients_df['Age'], bins=bins, labels=labels, right=True)


#각 나이대별 질병 빈도와 환자 수 계산
dis_counts_by_age = patients_df.groupby(['Age', 'Disease']).size().reset_index(name='Count')
patients_counts_by_age = patients_df.groupby('Age').size().reset_index(name='PatientCount')

#dis_counts_by_age와 patients_counts_by_age 병합
dis_counts_by_age = pd.merge(dis_counts_by_age, patients_counts_by_age, on='Age')

#각 나이대별 5% 이상 빈도인 질병만 필터링
dis_counts_by_age['Percentage'] = (dis_counts_by_age['Count'] / dis_counts_by_age['PatientCount']) * 100
filtered_dis_counts = dis_counts_by_age[dis_counts_by_age['Percentage'] >= 5]

#Age를 인덱스, Disease를 열, Count를 값으로 사용
pivoted_disease_counts = filtered_dis_counts.pivot_table(index='Disease', columns='Age', values='Count', aggfunc='sum', fill_value=0)

#데이터 시각화
plt.figure(figsize=(12, 8))
sns.heatmap(pivoted_disease_counts, annot=True, fmt="d", cmap="Blues", cbar_kws={'label': 'Disease Count'})

# 그래프
plt.title('Disease Frequency by Age', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Disease', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
