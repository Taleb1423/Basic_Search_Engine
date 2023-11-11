from elasticsearch import Elasticsearch
print("enter username:")
user = input()
print("enter password:")
pwd = input()

login = Elasticsearch(hosts="https://localhost:9200",basic_auth=[user,pwd], verify_certs=False)

key1 = login.security.create_api_key(name=user+"_key")
print("API key "+key1['name']+"created \n key is :"+key1['encoded'])
