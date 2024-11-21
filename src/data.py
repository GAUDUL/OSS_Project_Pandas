import os
import pandas as pd
print(os.getcwd())

file_path1='./data/Diseases_Symptoms.csv'
file_path2='./data/Medicine_Details.csv'
file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

dis_df=pd.read_csv(file_path1)
medi_df=pd.read_csv(file_path2)
patients_df = pd.read_csv(file_path3)

print('diseasesDf Columns: ')
print(dis_df.columns, end='\n\n')

print('medicineDf Coluimns: ')
print(medi_df.columns,end='\n\n')

print('patients_df Columns: ')
print(patients_df.columns, end='\n\n')

#print(medi_df['Excellent Review %'])

#Excellent Review 99.9 이상 필터링
#reivew99_medi_df = medi_df[medi_df['Excellent Review %'] >= 99.9]

#print(reivew99_medi_df)

