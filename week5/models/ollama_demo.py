from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

model=OllamaLLM(model='llama3.1:8b',temperature=1.5)

result=model.invoke("Give 5 indian male names?")

print(result)