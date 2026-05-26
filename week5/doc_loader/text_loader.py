from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template="Write a brief summary on given poem \n {text}",
    input_variables=["text"]
)

loader = TextLoader("cricket.txt",encoding='utf-8')

docs = loader.load()

doc_text = docs[0]

chain = prompt1 | model | parser

result = chain.invoke({"text": doc_text})

print(result)