from elasticsearch import Elasticsearch
import elasticsearch
import json
import pprint



body = {
    "query": {
        "match": {
            "movieId":"73319"
        }
    }
}



body_2 = {
    "query": {
        "match_phrase": {
            "genre":"sci"
        }
    }
}




#conectando ao ES
elastic_client = Elasticsearch(hosts=['http://192.168.150.128:9200'])
query = elastic_client.search(index="movies", body=body)
query = json.dumps(query, indent=10)
resp = json.loads(query)
pprint.pprint(resp)