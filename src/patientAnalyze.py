import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path3='./data/Disease_symptom_and_patient_profile_dataset.csv'

patients_df = pd.read_csv(file_path3) #환자 데이터셋 (증상: cough, fever, fatigue, difficulty breathing)

patient_info = patients_df[['Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']].copy()


#문자열로 작성돼있는 값들을 수치화 하기 위한 폼, Low는 1, Normal은 2, High는 3으로 치환
bp_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
chol_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
#Female은 1, Male은 2로 치환
gen_mapping={'Female':1, 'Male':2}

#Blood Pressure와 Cholesterol Level에 위의 폼 적용
patient_info['Blood Pressure'] = patient_info['Blood Pressure'].map(bp_mapping)
patient_info['Cholesterol Level'] = patient_info['Cholesterol Level'].map(chol_mapping)
patient_info['Gender']=patient_info['Gender'].map(gen_mapping)

graph=sns.pairplot(patient_info)

plt.show()
plt.close()