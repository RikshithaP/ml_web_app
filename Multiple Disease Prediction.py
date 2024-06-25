# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:02:17 2024

@author: riksh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Disease Prediction",
                   layout="wide")

diabetes_model = pickle.load(open('C:/Users/riksh/OneDrive/Desktop/ML Project/saved models/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/riksh/OneDrive/Desktop/ML Project/saved models/heart_model.sav','rb'))

cancer_model = pickle.load(open('C:/Users/riksh/OneDrive/Desktop/ML Project/saved models/breastcancer_model.sav','rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction' ,'Heart Disease Prediction','Breast Cancer Prediction'],
                           icons =['activity','heart','person'],
                           default_index = 0)
    
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')



    diab_diagnosis = ''



    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    
if selected == 'Heart Disease Prediction':

    
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')


    heart_diagnosis = ''


    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
if selected == 'Breast Cancer Prediction':
    
    
    st.title('Breast Cancer Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
    
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    
    with col1:
        mean_area = st.text_input('Mean Area')
    
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')
    
    with col3:
        mean_compactness = st.text_input('Mean Compactness')
    
    with col1:
        mean_concavity = st.text_input('Mean Concavity')
    
    with col2:
        mean_concave_points = st.text_input('Mean Concave Points')
    
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry')
    
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
    
    with col2:
        radius_error = st.text_input('Radius Error')
    
    with col3:
        texture_error = st.text_input('Texture Error')
    
    with col1:
        perimeter_error = st.text_input('Perimeter Error')
    
    with col2:
        area_error = st.text_input('Area Error')
    
    with col3:
        smoothness_error = st.text_input('Smoothness Error')
    
  
    breast_cancer_diagnosis = ''
    
  
    if st.button('Breast Cancer Test Result'):
        
       
        user_input = [
            mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
            mean_compactness, mean_concavity, mean_concave_points, mean_symmetry,
            mean_fractal_dimension, radius_error, texture_error, perimeter_error,
            area_error, smoothness_error
        ]
        
       
        user_input = [float(x) for x in user_input]
        
       
        breast_cancer_prediction = cancer_model.predict([user_input])
        
       
        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = 'The person is likely to have breast cancer'
        else:
            breast_cancer_diagnosis = 'The person is not likely to have breast cancer'
    
   
    st.success(breast_cancer_diagnosis)
