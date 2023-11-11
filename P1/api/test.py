#test file 
from P1.api.mymodule.elastic import client
from P1.api.mymodule.Pre_processing import index_doc

query=''
#index_doc("document.txt")
q= { "query-string" : {"query": query}}


res = client.search(index='studies',query=q)

print(res)
