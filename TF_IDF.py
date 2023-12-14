import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
stopwords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with']
vectorizer = TfidfVectorizer(stop_words=stopwords)





def compute_tfidf_vectors(file_path, vectorizer):
   with open(file_path) as f:
       data = json.load(f)
   review_texts = [entry['text'] for entry in data if entry['text'] is not None]
   X = vectorizer.fit_transform(review_texts)
   if os.path.exists("vectors.txt"):
      os.remove("vectors.txt")
   f=open("vectors.txt",'a')

   for vector in X :
      f.write(str(vector))
   return X


def search(query, docs, vectorizer):
  query_matrix = vectorizer.transform([query])
  similarity_scores = cosine_similarity(docs, query_matrix)
  
  return similarity_scores
   




res= search("super hero good bad best great ",compute_tfidf_vectors("dataset.json",vectorizer=vectorizer),vectorizer=vectorizer)
print(res)