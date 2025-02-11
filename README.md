LangChain DEMO Chatbot

This project is a simple chatbot built using Streamlit, LangChain, and Groq's LLM. It allows users to ask questions and receive responses from an AI-powered assistant.

Features

Uses LangChain for structured LLM interactions

Integrates Groq's LLM (Llama 3.3-70b-versatile)

Implements Streamlit for a simple web-based UI

Uses Environment Variables for API key security

Installation

Prerequisites

Python 3.8+

A Groq API Key

Streamlit and necessary dependencies

Setup

Clone the repository

git clone <repo_url>
cd <repo_folder>

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

Install dependencies

pip install -r requirements.txt

Set up environment variables

Create a .env file in the project root

Add the following lines:

GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here

Running the Chatbot

Run the following command to start the Streamlit app:

streamlit run app.py

Usage

Enter a question in the input field.

The chatbot processes the input using LangChain and Groq's model.

The response is displayed on the screen.

Dependencies

streamlit

langchain

langchain-core

langchain-groq

python-dotenv

Notes

Ensure you have valid API keys before running the application.

The assistant is designed to provide helpful responses but may have limitations.

License

This project is licensed under the MIT License.

Happy coding! 🚀

