
from P1.api.mymodule.elastic import client

settings1={ 
     "similarity": {
      "scripted_tfidf": {
        "type": "scripted",
        "script": {
          "source": "double tf = Math.sqrt(doc.freq); double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; double norm = 1/Math.sqrt(doc.length); return query.boost * tf * idf * norm;"
        }
      }
    },
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "whitespace",
          "filter": [ "stop","lowercase" ]
        }
      }
    }
  }

mapping1={  
        "dynamic_templates": [{
       "strings": {
          "match_mapping_type": "string",
          "mapping": {
            "type": "text",
                    "analyzer": "my_analyzer",
                    "similarity": "scripted_tfidf"
              }
            }
          
    }]
}

client.indices.create(index='studies',settings=settings1,mappings=mapping1)
