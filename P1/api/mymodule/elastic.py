from elasticsearch import Elasticsearch

key1= "NzVhMnY0c0JxRXVRNzdPdGNXTGg6OWdFdGFDd3dRZjJWaC1SQ0o1QmdFdw=="
client = Elasticsearch(
  "https://localhost:9200",
  api_key=key1,
verify_certs=False
)
