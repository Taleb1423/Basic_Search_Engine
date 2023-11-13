from elasticsearch import Elasticsearch

key1= "WkF5Wng0c0JCMTJJZFFXRTIyanU6dnZyS1dKbE5TajZBZUNrNFpwZHd5dw=="
client = Elasticsearch(
  "https://localhost:9200",
  api_key=key1,
verify_certs=False
)
