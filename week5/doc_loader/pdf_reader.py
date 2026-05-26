from langchain.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

# Load document
loader = TextLoader('docs.txt')
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = OpenAIEmbeddings()

# Vector DB
vectorstore = FAISS.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever()

# LLM (Chat model)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

query = "What is the key takeaway from the document?"

answer = qa_chain.invoke({"query": query})

print("Answer:", answer["result"])