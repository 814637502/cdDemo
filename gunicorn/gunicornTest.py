# -*-coding:utf-8 -*-
__author__ = 'sunyawei'

# gunicorn 测试  未成功 继续测试
def app(environ, start_response):
         data = b"Hello, World!\n"
         start_response("200 OK", [
             ("Content-Type", "text/plain"),
             ("Content-Length", str(len(data)))
         ])

         return iter([data])