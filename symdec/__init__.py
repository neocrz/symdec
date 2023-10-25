import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Symdec:

    def __init__(self, dataset: str) -> None:

        assert os.path.isfile(dataset), f"The path '{dataset}' is not a valid file"
        self.__vectorizer = TfidfVectorizer(stop_words="english")
        self.__dataset: str = dataset

    def load(self) -> None:
        df = pd.read_csv(self.__dataset)
        df = df.dropna(subset=['label', 'text'])

        doc = []

        for index, row in df.iterrows():
            label = row['label']
            text = row['text']
            
            doc.append((label, text))
        
        self.__deceases = [decease for decease, _ in doc]
        descriptions = [desc for _, desc in doc]
        
        
        self.__tfidf_matrix = self.__vectorizer.fit_transform(descriptions)

    def load_union(self) -> None:
        df = pd.read_csv(self.__dataset)
        df = df.dropna(subset=['label', 'text'])

        doc_dict = {}

        for index, row in df.iterrows():
            label = row['label']
            text = row['text']
            if label in doc_dict:
                doc_dict[label] += " " + text
            else:
                doc_dict[label] = text
        
        self.__deceases = list(doc_dict.keys())
        descriptions = list(doc_dict.values())
        
        
        self.__tfidf_matrix = self.__vectorizer.fit_transform(descriptions)

    def run(self, query: str) -> list:
        if not isinstance(query, str): 
            query = str(query)
        query_vector = self.__vectorizer.transform([query])

        cosine_similarities = cosine_similarity(query_vector, self.__tfidf_matrix)

        similarity_scores = list(enumerate(cosine_similarities[0]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)


        selected_deceases = set()
        result = []

        for index, score in similarity_scores:
            decease = self.__deceases[index]
            if decease not in selected_deceases:
                result.append((decease, score))
                selected_deceases.add(decease)
        return result