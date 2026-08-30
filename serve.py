from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import uvicorn
from langserve import add_routes

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain and local Ollama",
)

# Define prompt and model
prompt = ChatPromptTemplate.from_template("Give me a short summary about {topic}")
model = ChatOllama(model="llama2")
parser = StrOutputParser()

# Create the chain
chain = prompt | model | parser

# Add LangServe routes
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8125)