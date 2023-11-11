#test file 
from elastic import client

doc1={
'Title': 'The impact of exercise on cognitive function in older adults',
'Author': "Dr. John Smith",
'Topic': 'Exercise and cognitive function in older adults',
'Hypothesis': 'Engaging in regular exercise will improve cognitive function in older adults.',
'Result': 'The study found that older adults who engaged in regular exercise had better cognitive function than those who did not exercise.',
}
#client.create(index='studies',id=1,document=doc1)
query ="exercise"
q= { 
    "bool": { 
      "must": [
        { "match": { "Title":query},
          "match": {"Author":query},      
          "match": {"Result":query},
          "match": {"Hypotesis":query},
          "match": { "Topic":query}} 
        
      ],
    }
}
res =client.search(index='studies',query=q)
print(res)