from elasticsearch import Elasticsearch
import pandas as pd
import json

query_body = {

    'query':'select * from movies where movieId=1'
}

elastic_client = Elasticsearch(hosts=["192.168.150.128:9200"])


query_return = elastic_client.sql.query(body=query_body)
load_query = json.dumps(query_return, indent=10)
load_query_end = json.loads(load_query)


print(load_query_end)


with open('shakespeare2.json','w', encoding='utf-8') as j:
    json.dump(load_query_end,j, indent=2)

