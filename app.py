import streamlit as st
import numpy as np
import pickle
from predict import predicts
from sklearn.preprocessing import StandardScaler


def gender_encoder(gender):
    if gender.lower() == 'female':
        return 0  
    elif gender.lower() == 'male':
        return 1  

def smoking_encoder(smoking_history):
    if smoking_history.lower() == 'no info':
         return 0  
    elif smoking_history.lower() == 'never':
        return 4  
    elif smoking_history.lower() == 'former':
        return 3  
    elif smoking_history.lower() == 'current':
        return 1 
    elif smoking_history.lower() == 'not current':
        return 5  
    elif smoking_history.lower() == 'ever':
        return 2

st.title('Diabetes Prediction App')

gender = st.text_input('Input your gender(Female/Male):')   
age = st.text_input('Input your age:')
hypertension = st.text_input('Input your hypertension history (0 for no/ 1 for yes):')
heart_disease = st.text_input('Input your heart disease history (0 for no/ 1 for yes):')
smoking_history = st.text_input('Input your smoking history \n(No Info/ never/ former/current/not current/ever):')
bmi = st.text_input('Input your bmi:')
HbA1c_level = st.text_input('Input your HbA1c level:')
blood_glucose_level = st.text_input('Input your blood glucose level:')

if st.button('Diabetes Prediction Result:'):
    gender_encoded = gender_encoder(gender)
    smoking_history_encode = smoking_encoder(smoking_history)

    data = {
            'Gender': [gender_encoded],
            'Age': [age],
            'Hypertension': [hypertension],
            'Heart Disease': [heart_disease],
            'Smoking History': [smoking_history_encode],
            'BMI': [bmi],
            'HbA1c Level': [HbA1c_level],
            'Blood Glucose Level': [blood_glucose_level]
        }

    array = np.asarray(data).reshape(1,-1)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(array)

    prediction = predicts.predict(scaled_data)

    print(prediction)

    if prediction == 0:
        print('You are not diabetes')
    elif prediction == 1:
        print('You are diabetes')