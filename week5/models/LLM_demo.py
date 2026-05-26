from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gemini-1.5-pro')

result=llm.invoke('What is the capital of India?')

print(result)