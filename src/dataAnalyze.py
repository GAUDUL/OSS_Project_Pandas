import pandas as pd

file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

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

#데이터 요약 통계
print(patients_df.describe(), end='\n\n')

#Outcome Variable과 Age와의 관계
outcome_age_relation = patients_df.groupby(['Age', 'Outcome Variable']).size().unstack(fill_value=0)
outcome_age_relation['Positive Ratio'] = (outcome_age_relation['Positive'] / outcome_age_relation.sum(axis=1)) * 100
print(outcome_age_relation, end='\n\n')

#Outcome Variable과 BP와의 관계
outcome_BP_relation = patients_df.groupby(['Blood Pressure', 'Outcome Variable']).size().unstack(fill_value=0)
outcome_BP_relation['Positive Ratio'] = (outcome_BP_relation['Positive'] / outcome_BP_relation.sum(axis=1)) * 100
print(outcome_BP_relation, end='\n\n')

#Outcome Variable과 CL과의 관계
outcome_CL_relation = patients_df.groupby(['Cholesterol Level', 'Outcome Variable']).size().unstack(fill_value=0)
outcome_CL_relation['Positive Ratio'] = (outcome_CL_relation['Positive'] / outcome_CL_relation.sum(axis=1)) * 100
print(outcome_CL_relation, end='\n\n')