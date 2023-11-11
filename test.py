#test file 
from elastic import client
doc={
    "Author":"John smith",
    "contens":"djdewojoeiwcoiwecoiewncoienw jhon oiwqoidqwoijdqwoijdoi john wqjoioqwdjoiqj smith"
}
#client.index(index='studies', document=doc,id=1)

q= {    "match": {
              "Author": "John smith"
                        }
}



res = client.search(index='studies',query= q)
print(res)

