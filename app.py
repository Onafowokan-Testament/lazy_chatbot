import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate(
    [
        (
            "system",
            "You are a helpful lazy smart personal assisstant. Pleases respond to the users queries",
        ),
        ("user", "question: {question}"),
    ]
)

##streamlit framework

st.title("Langchain DEMO Chatbot")
input_text = st.text_input("Enter your question here")

llm = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke(input_text))
