import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import pandas as pd

# Configure the api_key

api = genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Streamlit Page

st.header("Healthcare Advisor")
input = st.text_input('''Hi! I am your medical expert.
                      Ask me information about Health, Diseases & Fitness only''')

submit = st.button('Submit')

# BMI Calculator

st.sidebar.subheader('BMI calculator')
weight = st.sidebar.text_input('Weight (in kg):')
height = st.sidebar.text_input('Height (in cm):')

# Calculate the BMI
weight = pd.to_numeric(weight)
height = pd.to_numeric(height)
height_mts = height/100
bmi = weight/(height_mts**2)

# Scale of the BMI

notes = f'''The BMI value can be interpreted as:
* Underweight: BMI < 18.5
* Normal weight: BMI 18.5 - 25
* Overweight: BMI 25 - 29.9
* Obese: BMI > 30'''

if bmi:
    st.sidebar.markdown("The BMI is: ")
    st.sidebar.write(bmi)
    st.sidebar.write(notes)

# Generative Ai Application

def get_response(text_input):
    model = genai.GenerativeModel("gemini-pro")
    if text_input!="":
        response  = model.generate_content(text_input)
        return(response.text)
    else:
        st.write("Please enter the Prompt !!!")

if submit:
    response = get_response(input)
    st.subheader("The :orange[Response] is: ")
    st.write(response)
    
# Disclaimer

st.subheader("Disclaimer: ", divider = True)
notes = f'''

1.This is an AI Advisor and should not be construed as a Medical Advise.
2. Before taking any action, it is recommended to consult a Medical practitioner.'''

st.markdown(notes)
    