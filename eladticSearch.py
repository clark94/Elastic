query_body = {

    'query':'select * from shakespeare limit 1'
}

#Parte Teorica

#O Elastic usa Docuntos para inserir os dados 

#Cluster : Database Name
#Indices : Tabelas
#Documentos : linha das Tabelas



#Importando a Biblioteca do ElasticSearch
from elasticsearch import Elasticsearch
import pandas as pd
import json

#Iniciando a Conexão junto ao Elastic Search
elastic_client = Elasticsearch(hosts=["192.168.150.128:9200"])

#verificando se o Indice existe
var1 = elastic_client.indices.exists("shakespeare")
print(var1)

#criando um indice no Elastic Search

#new_index = elastic_client.indices.create("robin")
#print(new_index)

#usando Sql
query_return = elastic_client.sql.query(body=query_body)
load_query = json.dumps(query_return, indent=10)
load_query_end = json.loads(load_query)
print(load_query_end)

