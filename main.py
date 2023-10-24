from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('data/Symptom2Disease.csv')

df = df.drop(columns=['Unnamed: 0'])
df = df.dropna(subset=['label', 'text'])
doc = []


for index, row in df.iterrows():
    label = row['label']
    text = row['text']
    
    doc.append((label, text))




documents = [desc for _, desc in doc]
deceases = [decease for decease, _ in doc]


vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents)

query = input("\nDigite a descrição dos sintomas (em inglês): ")
query_vector = vectorizer.transform([query])

cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)


similarity_scores = list(enumerate(cosine_similarities[0]))
similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)


selected_deceases = set()
result = []

for index, score in similarity_scores:
    decease = deceases[index]
    if decease not in selected_deceases:
        result.append((decease, score))
        selected_deceases.add(decease)

# Print dos resultados
print("\nDoenças ordenadas através da similaridade da descrição dos sintomas:")
for decease, score in result:
    print(decease, f"({score:.2f})")