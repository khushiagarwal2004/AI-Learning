from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant")
prompt1 = PromptTemplate(
    template="Write a brief summary on given pdf content \n {text}",
    input_variables=["text"]
)   
loader = PyPDFLoader("dl-curriculum.pdf")
docs= loader.load()
print(len(docs))