from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key="GOOGLE_API_KEY")
model=genai.GenerativeModel('gemini-pro')
def get_response(ques):
    response=model.generate_content(ques)
    return response.text
st.set_page_config(page_title="Lavish ChatBot")
st.header("Lavish SmartBot")
input=st.text_input("Input: ",key="Input")
Submit=st.button("Ask Question")
if(Submit):
    response=get_response(input)
    st.subheader("The Response is: ")
    st.write(response)
