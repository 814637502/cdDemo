# coding:utf-8
__author__ = 'sunyawei'

import redis
rc = redis.Redis(host='127.0.0.1')
ps = rc.pubsub()
# 创建一个新的频道，并且发布数据
ps.subscribe(["foo", "bar"])
rc.publish("foo", "hello i'm sange")
rc.publish("bar", "there is bar")