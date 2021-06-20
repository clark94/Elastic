import requests

requests = requests.get('http://192.168.150.128:9200/Shakespeare')

res = requests.json()

print(res)