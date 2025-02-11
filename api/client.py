import requests
import streamlit as st

def get_poem_response(text_input):
    response = requests.post(
        "http://localhost:8080/poem/invoke", json={"input": {"topic": text_input}}
    )
    return response.json()["output"]["content"]

def get_essay_response(text_input):
    response = requests.post(
        "http://localhost:8080/essay/invoke", json={"input": {"topic": text_input}}
    )
    return response.json()["output"]["content"]

st.title('Your essay buddy')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")
if input_text:
    st.write(get_essay_response(input_text))    

if input_text1:
    st.write(get_poem_response(input_text1))
