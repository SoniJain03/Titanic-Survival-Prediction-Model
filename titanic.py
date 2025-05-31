import streamlit as st
from joblib import load
st.title("Titanic Survival Prediction")

pclass=st.number_input("Enter Pclass (1,2,3)")
sex=st.radio("Enter Gender Female/Male", [0,1])
age=st.number_input("Enter age")
sibsp=st.number_input("Sibsp(0,1,2,3)")
parch=st.number_input("Parch (0,1,2)")
fare=st.number_input("Enter Fare")

clicked=st.button("Predict")

model=load("modeltitanic.joblib")

if clicked==True:
    #take the data and predict the survival/dead
    data=[pclass,sex,age,sibsp,parch,fare]
    print(data)

    pred=model.predict([data])[0]

    st.write(pred)

    # Show result in the web page
    if pred == 1:
        st.success("The passenger is likely to survive!")
    else:
        st.error("The passenger is likely not to survive.")


