import pandas as pd

df = pd.read_csv('movie_review.csv')
df.to_json('dataset.json', orient='records')
