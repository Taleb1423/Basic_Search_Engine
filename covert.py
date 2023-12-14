import pandas as pd

df = pd.read_csv('TWITTER_REVIEWS.csv')
df.to_json('dataset.json', orient='records')
