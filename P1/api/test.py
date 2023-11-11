#test file 
from elastic import client
from Pre_processing import index_doc



#index_doc("document.txt")

q= { "match" : {"Objective": "The"}}


res = client.search(index='studies',query=q)

print(res['hits']['hits'])
