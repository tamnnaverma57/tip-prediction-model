import streamlit as st
import pickle
import pandas as pd
model=pickle.load(open('tips_model.pkl','rb'))
st.title("Tip Prediction App")
total_bill=st.number_input("total bill")
size= st.number_input("Size")
sex=st.selectbox("Sex",['Male','Female'])
smoker=st.selectbox("Smoker",['Yes','No'])
day=st.selectbox("Day",['Thur','Fri','Sat','Sun'])
time=st.selectbox("Time",['Lunch','Dinner'])
input_data=pd.DataFrame({
    'total_bill':[total_bill],  
    'sex':[sex],
    'day':[day],
    'time':[time]
    })
if st.button("Predict Tip"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip:{predicted[0]:.2f}")