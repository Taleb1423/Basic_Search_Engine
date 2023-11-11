from elasticsearch import Elasticsearch

key1= "TU0yWHVvc0JiRlpVYTZHR1NaazM6WnRZR3BNREtSLU9uRXJ5OS10VzBVZw=="
client = Elasticsearch(
  "https://localhost:9200",
  api_key=key1,
verify_certs=False
)
