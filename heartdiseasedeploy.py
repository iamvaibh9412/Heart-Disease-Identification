#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st
import matplotlib as plt
import matplotlib.image as mp
import joblib
from sklearn.preprocessing import LabelEncoder
import pickle as pkl




st.set_page_config(page_title= "Heart Disease Detection Machine learning App",layout = "wide")
st.header("***HEART DISEASE IDENTIFICATION***")
image = mp.imread("heartImg.jpg")
st.image(image)
st.write("""
    **Heart Disease Detection Machine learning App**
    In this implimentation various **Mechine learning** agorithms are used in this app for building a **classification model** to **Detect heart disease**
    """
    ) 

 
st.sidebar.write("***CHECK DO YOU HAVE HEART DISEASE?***")

BMI = st.sidebar.number_input("Enter your BMI", 0,100)
Smoking = st.sidebar.radio("Do you smoke?",["Yes","No"])
AlcoholDrinking =st.sidebar.radio("Are you alcoholic?",["Yes","No"]) 
Stroke =st.sidebar.radio("Do you have Stroke?",["Yes","No"])
PhysicalHealth = st.sidebar.radio("Do you have PhysicalHealth?",["Yes","No"])
MentalHealth = st.sidebar.radio("Are you okey with mental health?",["Yes","No"])
DiffWalking = st.sidebar.radio("Do you DiffWalking?",["Yes","No"]) 
Sex = st.sidebar.radio("Gender",["Male","Female"]) 
AgeCategory = st.sidebar.selectbox("Chose your Age range",['55-59', '80 or older', '65-69', '75-79', '40-44', '70-74',
       '60-64', '50-54', '45-49', '18-24', '35-39', '30-34', '25-29'])
Race = st.sidebar.radio("Which is your race",['White', 'Black', 'Asian', 'American Indian/Alaskan Native','Other', 'Hispanic']) 
Diabetic = st.sidebar.radio("Do you have Diabetic?",["Yes","No"])
PhysicalActivity = st.sidebar.radio("Are you doing Workouts?",["Yes","No"]) 
GenHealth = st.sidebar.radio("GenHealth?",["Yes","No"])
SleepTime = st.sidebar.selectbox("how long do you sleep",[5,7,  8,  6, 12,  4,  9, 10, 15,  3,  2,  1, 16,
       18, 14, 20, 11, 13, 17, 24, 19, 21, 22, 23])
Asthma = st.sidebar.radio("Do you have Asthma?",["Yes","No"])
KidneyDisease = st.sidebar.radio("Do you have kidney disease?",["Yes","No"]) 
SkinCancer = st.sidebar.radio("Do you have Skin cancer?",["Yes","No"]) 



test = [["BMI","Smoking","AlcoholDrinking","Stroke","PhysicalHealth","MentalHealth","DiffWalking","Sex","AgeCategory","PhysicalActivity","GenHealth","SleepTime","Asthma","KidneyDisease","SkinCancer"]]

test = pd.DataFrame([{"BMI" : BMI,"Smoking" : Smoking,"AlcoholDrinking" : AlcoholDrinking,"Stroke" : Stroke,"PhysicalHealth":PhysicalHealth,"MentalHealth" : MentalHealth, "DiffWalking": DiffWalking, "Sex": Sex, "AgeCategory" : AgeCategory, 
    "Race": Race,"Diabetic": Diabetic , "PhysicalActivity":PhysicalActivity,"GenHealth" : GenHealth,"SleepTime":SleepTime,"Asthma":Asthma,"KidneyDisease" : KidneyDisease,"SkinCancer" : SkinCancer}])

st.write("***PREVIEW OF YOUR DATA***")
st.write(test)

clse = ["Smoking","AlcoholDrinking","Stroke","PhysicalHealth","Diabetic","MentalHealth","DiffWalking","PhysicalActivity","GenHealth","Asthma","KidneyDisease","SkinCancer"]

for x in clse:
    for i in test[x]:
        if i == "Yes":
            test[x] = 1
        else:
            test[x] = 0

for i in test["Sex"]:
    if i == "Male":
        test["Sex"] = 1
    else:
        test["Sex"] = 0

for i in test["AgeCategory"]:
    if i == "25-29":
        test["AgeCategory"] = 1
    elif i == "18-24":
        test["AgeCategory"] = 0
    elif i == "30-34":
        test["AgeCategory"] = 2
    elif i == "35-39":
        test["AgeCategory"] = 3
    elif i == "40-44":
        test["AgeCategory"] = 4
    elif i == "40-44":
        test["AgeCategory"] = 5
    elif i == "45-49":
        test["AgeCategory"] = 5
    elif i == "50-54":
        test["AgeCategory"] = 6
    elif i == "55-59":
        test["AgeCategory"] = 7
    elif i == "60-64":
        test["AgeCategory"] = 8
    elif i == "65-69":
        test["AgeCategory"] = 9
    elif i == "70-74":
        test["AgeCategory"] = 10
    elif i == "75-79":
        test["AgeCategory"] = 11
    else:
        test["AgeCategory"] = 12	

gg = ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic',
       'Other', 'White']


for i in test["Race"]:
    if i ==gg[0]:
        test["Race"] = 0
    elif i ==gg[1]:
        test["Race"] = 1
    elif i ==gg[2]:
        test["Race"] = 2
    elif i ==gg[3]:
        test["Race"] = 3
    elif i ==gg[4]:
        test["Race"] = 4
    else:
        test["Race"] = 5


model = pkl.load(open("finalDump.p","rb"))


st.write("***RESULT:***")

#st.write(prediction)
def result():
    prediction = model.predict(test)
    if prediction == 0:
        results = "DONT WORRY! YOU HAVE NO HEART DISEASE"
    else:
        results = "HEART DISEASE DETECTED!! YOU NEED TO CONSULT A DOCTOR IMMEDIATELY"
    return results


results = result()

btn = st.sidebar.button("Submit",on_click=st.write(results))

