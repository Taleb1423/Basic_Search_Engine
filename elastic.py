from elasticsearch import Elasticsearch

key1= "SUU0VHJvc0IwbnJPM2JHOE9wVnE6UWMxelZFNHpUMldyc1pETFNRMVNKUQ=="
client = Elasticsearch(
  "https://localhost:9200",
  api_key=key1,
verify_certs=False
)
