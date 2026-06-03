from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-R1-0528',
    task='text-generation',    
)
model=ChatHuggingFace(llm=llm)

paper_input=st.selectbox('Sleect Research Paper Name',['Select...','Attention is all you need','BERT:Pre-training of deep Bidirectional Transformers','GPT-3:Language Models are few-Shot Learners','Diffusion Models Beat GANs on Image Synthesis'])

style_input=st.selectbox('Selct Explanation Style',['Beginner-friendly','Technical','Code-oriented','Mathematical'])

length_input=st.selectbox('Select Explanation Length',['Short(1-2 Para)','Medium(3-4 para)','Long(Deatail explanation)'])

template=load_prompt('template.json')



if st.button('Summarize'):
    chain=template | model
    result=chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })     
    st.write(result.content) 
