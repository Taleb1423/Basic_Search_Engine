from elasticsearch import Elasticsearch

key1= "ZDZZUnY0c0JRZEIzRnJRSVpVLWc6dWY3a1VOTF9SM0dxLVBkSUhINGRaZw=="
client = Elasticsearch(
  "https://localhost:9200",
  api_key=key1,
verify_certs=False
)
