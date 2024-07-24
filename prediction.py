import tensorflow as tf
import pandas as pd

# Change this path to your csv file location
dataset_path = 'Dataset/test_data.csv'


loaded_model = tf.keras.models.load_model('attrition_model.keras')
df_original = pd.read_csv(dataset_path)
df = df_original.copy()
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No':0}).astype('int64')
selected_features = [
    'BusinessTravel', 'Department', 'EducationField', 'JobRole', 'MaritalStatus',
    'OverTime', 'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction',
    'Age', 'DailyRate', 'DistanceFromHome', 'JobLevel', 'NumCompaniesWorked',
    'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsWithCurrManager'
]
df = df[selected_features]
df = pd.get_dummies(df, dtype='int64')
max_ = df.max()
min_ = df.min()
df = (df - min_) / (max_ - min_)
y_pred = loaded_model.predict(df)
y_pred = (y_pred > 0.5).astype('int32').reshape(-1)


df_original['Attrition'] = y_pred
df_original.to_csv(dataset_path, index=None)