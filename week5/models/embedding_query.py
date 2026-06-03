from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
 
sentences = ["This is an example sentence", "Each sentence is converted"]
 
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
 
 
document = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
 
embeddings2 = model.encode(document)
 
query = "Who is former indian captain?"
 
queryEmbed = model.encode([query])
 
scores = model.similarity(embeddings2,queryEmbed)
 
print(scores)
 
index , score = sorted(enumerate(scores),key=lambda x :x[-1])[-1]
 
print(index,score)
print(query)
print(document[index])