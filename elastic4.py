import requests
import json

headers = {

    'Content-Type: application/json'
}



def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match_phrase": {
                "text_entry": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results




print(search('http://192.168.150.128:9200/shakespeare/_search',''))

