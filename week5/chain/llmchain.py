from langchain_GoogleOpenAI import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# Load LLM (GPT-3.5 Turbo)
llm=OpenAI(model='gpt-3.5-turbo',temperature=0.7)

# Create a Prompt Template
prompt=PromptTemplate(
    template='Suggest a catchy blog title about {topic}',
    input_variables=['topic']
)

# Create an LLM Chain
chain=LLMChain(llm=llm,prompt=prompt)

# Run the chain with an input
topic=input('Enter a topic: ')
output=chain.run(topic)

print('Generated Blog Title:',output)