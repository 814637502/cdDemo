#-*- coding:utf-8-*-
import json
import datetime
from elasticsearch import Elasticsearch

__author__ = 'sunyawei'
#


es = Elasticsearch('localhost:9200');
# 这里是可以定义好模板的，定义好模板就可以直接加到index中
st_people=dict({"name": "syw", "sex": "very man", "weight": '135'})
people__mapping={
    "name": "林妹妹",
    "sex": "man",
    "weight": "135"
}


# 如果索引不存在，则创建索引sssssssssssssssss

if es.indices.exists(index='syw-index') is not True:
    es.create(index="syw-index", doc_type="syw_type",
              id="001", body=st_people)
# people__mapping["name"]="sunaywei .
people__mapping["weight"] = "120"
people01 = people__mapping
# es.index(index="syw-index",body=people01,id=None,doc_type="syw_type")
# es.index(index="syw-index",body=people01,id=None,doc_type="syw_type")
# is_delete=es.delete( index="syw-index", doc_type="syw_type", id="sh-nSWMBpyt9EfgvefOt")
# print(is_delete)
# query={"query":{
#     "term":{"name.keyword":"林妹妹"}
# }}

'''这个是自己找的多条件查询的结构'''
# query={"query":{'bool':{"must":[{"term":
#                                      {"name.keyword":
#                                           "林妹妹"}}
#                                 ,{"range":{"weight":{"lt":130}}}
# ]}
# }}
''''''
query = {"query": {"filtered": {{"filter": {"range": {"weight": {"lt": "130"}}}}, {"query": {"match": {"name": "玲妹妹"}}}
                                }
                   }
        }


print(query)
a = es.search(index=None, doc_type=None, body=query)
print("a==============  "+json.dumps(a))
for aa in a['hits']['hits']:

    print(aa['_source'])
    pass
query = {"query": {"range": {"weight": {"lt": 130}}}}

# count =es.delete_by_query(index=None,body=query,doc_type=None,id=None)
# print("a==============  "+json.dumps(count['hits']['hits']))
