import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import unicodedata, re, itertools, sys

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories)
control_char_re = re.compile('[%s]' % re.escape(control_chars))

def remove_control_chars(s):
   return control_char_re.sub('', s)
import re

def remove_special_chars(s):
   return re.sub('[^A-Za-z0-9 ]+', '', s)

def remove_alphanumeric_chars(s):
   return ''.join(e for e in s if not e.isalnum())

def compute_tfidf_vectors(file_path):
   with open(file_path) as f:
       data = json.load(f)

   review_texts = [remove_control_chars(remove_special_chars(remove_alphanumeric_chars(entry['review_text']))) for entry in data if entry['review_text'] is not None]

   vectorizer = TfidfVectorizer(stop_words=['the', 'is', 'at', 'which', 'on'])
   X = vectorizer.fit_transform(review_texts)

   tfidf_vectors = X.toarray().tolist()

   return tfidf_vectors


print(compute_tfidf_vectors("dataset.json"))