# coding:utf-8
__author__ = 'sunyawei'

import redis
rc = redis.Redis(host='127.0.0.1')
ps = rc.pubsub()
# 客户端对频道进行关注
ps.subscribe(['foo', 'bar'])
# 监听类型是message的 取出来数据
for ite in ps.listen():
    print(ite["type"])
    if ite["type"] == 'message':
        print(ite['data'])

