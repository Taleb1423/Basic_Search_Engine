from elasticsearch import Elasticsearch

client = Elasticsearch(
    'https://localhost:9200',
    basic_auth=['elastic', '+4BUBOSF4W=0pmpACjb='],
    verify_certs=False
)

print(client.search(index='my-index'))