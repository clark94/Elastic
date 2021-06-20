query_body = {
  "query": {
      "match_phrase": {
          "text_entry": "to be or not to be"
      }
  }
}


import json
from elasticsearch import Elasticsearch
elastic_client = Elasticsearch(hosts=["192.168.150.128:9200"])
result = elastic_client.search(index="shakespeare", body=query_body)

resp = json.dumps(result,indent=5)

print('de certo')

with open('arq.json','w', encoding='utf-8') as j:
    json.dump(result,j,indent=5)

