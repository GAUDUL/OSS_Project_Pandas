import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

file_path3 = './data/Disease_symptom_and_patient_profile_dataset.csv'

patients_df = pd.read_csv(file_path3)

# 문자열을 수치화하기 위한 매핑
bp_mapping = {'Low': 1, 'Normal': 2, 'High': 3}
chol_mapping = {'Low': 1, 'Normal': 2, 'High': 3}

# 매핑 적용
patients_df['Blood Pressure'] = patients_df['Blood Pressure'].map(bp_mapping)
patients_df['Cholesterol Level'] = patients_df['Cholesterol Level'].map(chol_mapping)

#Age구간 나누기
bins = [10, 19, 29, 39, 49, 59, 69, 79, 89, 99]  # 구간 정의
labels = ['10~19', '20~29', '30~39', '40~49', '50~59', '60~69', '70~79', '80~89', '90~99']  # 구간 레이블
patients_df['Age Group'] = pd.cut(patients_df['Age'], bins=bins, labels=labels, right=True)

# 특성 및 레이블 정의
X = patients_df[['Age', 'Blood Pressure', 'Cholesterol Level']]
y = patients_df['Disease']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 특성 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# 모델 평가
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 하이퍼파라미터 튜닝 (GridSearchCV)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
grid_search.fit(X_train_scaled, y_train)

# 최적 모델 출력
best_model = grid_search.best_estimator_
print(f"Best Parameters: {grid_search.best_params_}")

# 최적 모델 평가
y_pred_best = best_model.predict(X_test_scaled)
print(f"Best Model: {accuracy_score(y_test, y_pred_best):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_best))

# 새로운 데이터 예측 (예: 나이=37세)
new_patient = pd.DataFrame([[37, 2, 2]], columns=['Age', 'Blood Pressure', 'Cholesterol Level'])

# 나이에 따라 구간 나누기
new_patient['Age Group'] = pd.cut(new_patient['Age'], bins=bins, labels=labels, right=True)

# 스케일링 적용
new_patient_scaled = scaler.transform(new_patient[['Age', 'Blood Pressure', 'Cholesterol Level']])

# 예측 수행
predicted_disease = best_model.predict(new_patient_scaled)[0]
print(f"Predicted Disease (Age {new_patient['Age'][0]}, Age Group: {new_patient['Age Group'][0]}): {predicted_disease}")
