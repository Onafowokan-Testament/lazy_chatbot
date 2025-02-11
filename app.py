from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import sequential
from langchain_core.outPut_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import streamlit as st

