from elasticsearch import Elasticsearch, VERSION

body={"doc": {
                'title': 'Sabrina',
                
            }}


#Primeiro passo Conectar a Instância do Elastic
elastic_client = Elasticsearch(hosts=['192.168.150.128:9200'])

#Criar o indice filmes
# filmes = elastic_client.indices.create("movies")
# print(filmes)



# elastic_client.indices.delete(index="movies")
# print(elastic_client)


# coll.update(index='stories-test',doc_type='news',id=hit.meta.id,
#                 body={"doc": {"stanford": 1, "parsed_sents": parsed }})



res = elastic_client.get(index="movies", doc_type="movies", id="ZRnZ4XkBvFimIuU8XKDI", ignore=404)

#if_seq_no, #if_primary_term=  #retry_on_conflict=
update = elastic_client.update(index="movies", doc_type="movies",id="ZRnZ4XkBvFimIuU8XKDI" , body=body)

#print(update)

print(res)

#ZRnZ4XkBvFimIuU8XKDI
#delete1 = elastic_client.delete(index="movies", doc_type="movies", id="ZRnZ4XkBvFimIuU8XKDI")
#print(delete1)




