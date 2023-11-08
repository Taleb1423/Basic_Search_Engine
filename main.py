#test file 
from elastic import client

client = Elasticsearch(
  "https://localhost:9200",
  api_key="THdxbHJZc0JoNFNac3N2T082Rjk6NjBpRDR6MWlRNmF3am1saGVXZ1NWQQ==",
verify_certs=False
)
    
d
client.index(index='my_index', document=doc,id=1)

q= {    "match": {
              "Author": "John smith"
                        }
}



res = client.search(index='studies',query= q)
print(res)

