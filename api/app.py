import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes

load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Chatbot",
    description="This is a simple lazy chatbot using langchain",
    version="1.0",
)

model = ChatGroq()
prompt_template1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt_template2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} with 100 words"
)
output_parser = StrOutputParser()


add_routes(app, prompt_template1 | model, path="/essay")
add_routes(app, prompt_template2 | model, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
