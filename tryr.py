import requests

query_body = {
  "query": {
      "match_phrase": {
          "text_entry": "to be or not to be"
      }
  }
}

headers = {
    'Content-Type: application/json'

      "query": {
      "match_phrase": {
          "text_entry": "to be or not to be"
      }
  }
}

uri = 'http://192.168.150.128:9200:9200/shakespeare/_search?'


requests = requests.get(uri, headers=headers)
resp = requests.json()