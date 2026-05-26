# Deprecated code
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm=OpenAI(model='gpt-3.5-turbo',temperature=0.7)

# Create a Prompt Template
prompt=PromptTemplate(
    template='Suggest a catchy blog title about {topic}',
    input_variables=['topic']
)

# Define Input
topic=input('Enter a topic')

# Format the prompt manually using PromptTemplate
formated_prompt=prompt.format(topic=topic)

# Call the LLM directly 
blog_tile=llm.predict(formated_prompt)

# Print the output
print('Generated Blog Title:',blog_tile)