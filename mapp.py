from elasticsearch import Elasticsearch

self.elastic_con = Elasticsearch([host], verify_certs=True)
mapping = '''
{  
  "mappings":{  
    "logs_june":{  
      "_timestamp":{  
        "enabled":"true"
      },
      "properties":{  
        "logdate":{  
          "type":"date",
          "format":"dd/MM/yyy HH:mm:ss"
        }
      }
    }
  }
}'''
self.elastic_con.indices.create(index='test-index', ignore=400, body=mapping)