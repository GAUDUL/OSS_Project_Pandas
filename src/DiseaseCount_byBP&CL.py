import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

patients_df = pd.read_csv(file_path3) #환자 데이터셋 (증상: cough, fever, fatigue, difficulty breathing)

#결과가 Positive인 환자들의 데이터만 가져오기
patients_df = patients_df[patients_df['Outcome Variable'] == 'Positive']

#문자열로 작성돼있는 값들을 수치화 하기 위한 폼, Low는 1, Normal은 2, High는 3으로 치환
bp_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
chol_mapping = {'Low': 1, 'Normal': 2, 'High': 3}

#Blood Pressure와 Cholesterol Level에 위의 폼 적용
patients_df['Blood Pressure'] = patients_df['Blood Pressure'].map(bp_mapping)
patients_df['Cholesterol Level'] = patients_df['Cholesterol Level'].map(chol_mapping)


#혈압 수치별 질병 빈도와 환자 수 계산
dis_counts_by_BP = patients_df.groupby(['Blood Pressure', 'Disease']).size().reset_index(name='Count')
patients_counts_by_BP = patients_df.groupby('Blood Pressure').size().reset_index(name='PatientCount')

#콜레스테롤 수치별 질병 빈도와 환자 수 계산
dis_counts_by_CL= patients_df.groupby(['Cholesterol Level', 'Disease']).size().reset_index(name='Count')
patients_counts_by_CL = patients_df.groupby('Cholesterol Level').size().reset_index(name='PatientCount')

#dis_counts_by_BP와 patients_counts_by_BP 병합
dis_counts_by_BP = pd.merge(dis_counts_by_BP, patients_counts_by_BP, on='Blood Pressure')

#dis_counts_by_CL과 patients_counts_by_CL 병합
dis_counts_by_CL = pd.merge(dis_counts_by_CL, patients_counts_by_CL, on='Cholesterol Level')

#각 Blood Pressure 수치별 2% 이상 빈도인 질병만 필터링
dis_counts_by_BP['Percentage'] = (dis_counts_by_BP['Count'] / dis_counts_by_BP['PatientCount']) * 100
filtered_dis_counts_BP = dis_counts_by_BP[dis_counts_by_BP['Percentage'] >= 2]

#각 Cholesterol Level 별 2% 이상 빈도인 질병만 필터링
dis_counts_by_CL['Percentage'] = (dis_counts_by_CL['Count'] / dis_counts_by_CL['PatientCount']) * 100
filtered_dis_counts_CL = dis_counts_by_CL[dis_counts_by_CL['Percentage'] >= 2]

#BloodPressure를 인덱스, Disease를 열, Count를 값으로 사용
pivoted_BP_disease_counts = filtered_dis_counts_BP.pivot_table(index='Disease', columns='Blood Pressure', values='Count', aggfunc='sum', fill_value=0)

#Cholesterol Level을 인덱스, Disease를 열, Count를 값으로 사용
pivoted_CL_disease_counts = filtered_dis_counts_CL.pivot_table(index='Disease', columns='Cholesterol Level', values='Count', aggfunc='sum', fill_value=0)


#혈압에 따른 질병 빈도 데이터 시각화
plt.figure(figsize=(12, 8))
sns.heatmap(pivoted_BP_disease_counts, annot=True, fmt="d", cmap="Blues", cbar_kws={'label': 'Disease Count'})

# 그래프
plt.title('Disease Frequency by Blood Pressure', fontsize=16)
plt.xlabel('Blood Pressure', fontsize=12)
plt.ylabel('Disease', fontsize=12)
plt.xticks(ticks=[0.5, 1.5, 2.5], labels=['Low', 'Normal', 'High'], rotation=45)
plt.tight_layout()

plt.show()

#콜레스테롤 수치에 따른 질병 빈도 데이터 시각화
plt.figure(figsize=(12, 8))
sns.heatmap(pivoted_CL_disease_counts, annot=True, fmt="d", cmap="Blues", cbar_kws={'label': 'Disease Count'})

# 그래프
plt.title('Disease Frequency by Cholesterol Level', fontsize=16)
plt.xlabel('Cholesterol Level', fontsize=12)
plt.ylabel('Disease', fontsize=12)
plt.xticks(ticks=[0.5, 1.5, 2.5], labels=['Low', 'Normal', 'High'], rotation=45)
plt.tight_layout()

plt.show()
