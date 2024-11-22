import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path1='./data/Diseases_Symptoms.csv'
file_path2='./data/Medicine_Details.csv'
file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

dis_df=pd.read_csv(file_path1) #질병 데이터셋
medi_df=pd.read_csv(file_path2) #약 데이터셋
patients_df = pd.read_csv(file_path3) #환자 데이터셋 (증상: cough, fever, fatigue, difficulty breathing)

#medi_df에서 Excellent Review 99.9 이상이고 Poor Review 1 미만인 약들 필터링
filteredmedi_df = medi_df[(medi_df['Excellent Review %'] >= 99.9) & (medi_df['Poor Review %'] < 1)]
print(filteredmedi_df, end='\n\n')

#dis_df의 Symptoms열에서 'cough', 'fever', 'fatigue', 'difficulty breathing' 단어가 포함된 행만 필터링
filtered_diseases_df = dis_df[dis_df['Symptoms'].str.contains('cough|fever|fatigue|difficulty breathing', case=False, na=False)]
print(filtered_diseases_df, end='\n\n')
