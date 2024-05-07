import numpy as np
import pandas as pd
import pickle
import sklearn
import streamlit as st

pickle_in = open("LogisticRegression2.pkl","rb")
log_reg = pickle.load(pickle_in)

def student_dropout_analysis(input_data):
# change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = log_reg.predict(input_data_reshaped)
    #print(prediction)

    if (prediction[0]== 0):
       return 'No Dropout'
    else:
       return 'Dropout'


def main():
    st.title("Student Dropout Prediction")
    Marital_status = st.text_input("Marital_status")
    Application_mode = st.text_input("Application_mode")
    Application_order = st.text_input("Application_order")
    Course = st.text_input("Course")
    Daytime_evening_attendance = st.text_input("Daytime_evening_attendance")
    Previous_qualification = st.text_input("Previous_qualification")
    Nationality =  st.text_input("Nationality")
    Mother_qualification = st.text_input("Mother_qualification")
    Father_qualification = st.text_input("Father_qualification")
    Mother_occupation = st.text_input(" Mother_occupation")
    Father_occupation = st.text_input("Father_occupation")
    Displaced = st.text_input("Displaced")
    Educational_special_needs= st.text_input("Educational_special_needs")
    Debtor = st.text_input(" Debtor")
    Tuition_fees_up_to_date = st.text_input("Tuition_fees_up_to_date")
    Gender = st.text_input(" Gender")
    Scholarship_holder = st.text_input("Scholarship_holder ")
    Age_at_enrollment = st.text_input("Age_at_enrollment")
    International = st.text_input("International")

    Curricular_units_1st_sem_credited = st.text_input("Curricular_units_1st_sem_credited")
    Curricular_units_1st_sem_enrolled = st.text_input("Curricular_units_1st_sem_enrolled")
    Curricular_units_1st_sem_evaluations = st.text_input("Curricular_units_1st_sem_evaluations")
    Curricular_units_1st_sem_approved = st.text_input("Curricular_units_1st_sem_approved")
    Curricular_units_1st_sem_grade = st.text_input("Curricular_units_1st_sem_grade")
    Curricular_units_1st_sem_without_evaluations =  st.text_input("Curricular_units_1st_sem_without_evaluations")

    Curricular_units_2nd_sem_credited = st.text_input("Curricular_units_2nd_sem_credited")
    Curricular_units_2nd_sem_enrolled = st.text_input("Curricular_units_2nd_sem_enrolled")
    Curricular_units_2nd_sem_evaluations = st.text_input(" Curricular_units_2nd_sem_evaluations")
    Curricular_units_2nd_sem_approved = st.text_input("Curricular_units_2nd_sem_approved")
    Curricular_units_2nd_sem_grade = st.text_input("Curricular_units_2nd_sem_grade")
    Curricular_units_2nd_sem_without_evaluations = st.text_input("Curricular_units_2nd_sem_without_evaluations")

    Unemployment_rate = st.text_input("Unemployment_rate")
    Inflation_rate = st.text_input("Inflation_rate")
    GDP = st.text_input("GDP")

    # Convert the dtype to numeric -
    numeric_inputs = []
    try:

        numeric_inputs = [
        int(Marital_status), 
        int(Application_mode),
        int(Application_order), 
        int(Course),
        int(Daytime_evening_attendance), 
        int(Previous_qualification),
        int(Nationality), 
        int(Mother_qualification),
        int(Father_qualification), 
        int(Mother_occupation),
        int(Father_occupation), 
        int(Displaced),
        int(Educational_special_needs), 
        int(Debtor),
        int(Tuition_fees_up_to_date), 
        int(Gender),
        int(Scholarship_holder), 
        int(Age_at_enrollment),
        int(International), 
        int(Curricular_units_1st_sem_credited),
        int(Curricular_units_1st_sem_enrolled), 
        int(Curricular_units_1st_sem_evaluations),
        int(Curricular_units_1st_sem_approved), 
        float(Curricular_units_1st_sem_grade),
        int(Curricular_units_1st_sem_without_evaluations), 
        int(Curricular_units_2nd_sem_credited),
        int(Curricular_units_2nd_sem_enrolled), 
        int(Curricular_units_2nd_sem_evaluations),
        int(Curricular_units_2nd_sem_approved), 
        float(Curricular_units_2nd_sem_grade),
        int(Curricular_units_2nd_sem_without_evaluations), 
        float(Unemployment_rate),
        float(Inflation_rate), 
        float(GDP)
    ]
    except ValueError:
        st.error("Please enter valid numeric values.")
    
        
    result = ""
    if st.button("Prediction"):
        result= student_dropout_analysis(numeric_inputs)
    st.success(result)


if __name__=='__main__':
    main()
    