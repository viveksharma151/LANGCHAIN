import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama  # Updated import

# Load environment variables
load_dotenv()

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

# Streamlit Interface
st.title("LangChain Demo with Llama2 (Ollama)")
input_text = st.text_input("Search the topic you want")

# Initialize Local LLM via Ollama
llm = ChatOllama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))