import streamlit as st
import numpy as np
import requests
import pandas as pd

st.header("Predicting :blue[Loan] Acceptance", divider = True)

def predict(features):
    """ this function will recieve features as input and sends
        the ordered features as array to the flask server
        and returns the response of the flask server which is
        the predicted value
    """
    endpoint = 'http://127.0.0.1:5000/predict'
    features = features.tolist() #convert numpy array to python list
    data =  {
                "features" : features
            }
    try:
        response = requests.post(endpoint, json = data)
        return response.json()["prediction"]
        
    except Exception as e:
        st.error(f"Error predicting the model: {str(e)}")
        return None



with st.expander("Predict Loan Approval", expanded = True):
    st.subheader("Enter data")
   
    Income_pred = st.number_input("Income", min_value = 0, value = 50000)
    Credit_Score_pred = st.number_input("Credit Score", min_value = 0, value = 400)
    Loan_Amount_pred = st.number_input("Loan Amount", min_value = 0, value = 1000)
    DTI_Ratio = st.number_input("DTI Ratio", min_value = 0, value = 7)
    Employment_Status = st.selectbox("Employment Status", ("Employed","Unemployed"))

        
    Employment_Status_encoded = 0 if Employment_Status == "Employed" else 1

     
    features = np.array([Income_pred,Credit_Score_pred,Loan_Amount_pred,DTI_Ratio,Employment_Status_encoded])

    if st.button("Predict"):
        with st.spinner("Calculating.."):
            predicted = predict(features)
            st.success(f"{predicted}")



"_by Shehab_"
